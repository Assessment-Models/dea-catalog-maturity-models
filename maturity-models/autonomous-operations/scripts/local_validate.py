#!/usr/bin/env python3
"""Local validation for the autonomous-operations asset bundle.

Checks: catalog entry schema (CI-equivalent), exactly 5 levels, per-level fields,
split-file consistency with the catalog entry, unique criterion ids/names, canonical
band ranges from index.yaml, dimension weights sum to 1, an OODA progression and loop
driver on every level, and a hygiene scan that rejects legacy external-framework
references. Hygiene patterns are assembled at runtime from fragments so that this
file itself contains no banned literal. Run from the bundle directory:
    python3 scripts/local_validate.py
"""
import os, re, sys, glob
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
BUNDLE = os.path.dirname(HERE)  # maturity-models/autonomous-operations
CATALOG_ENTRY = os.path.join(os.path.dirname(BUNDLE), "v1-alpha", "autonomous-operations.yaml")
INDEX = os.path.join(os.path.dirname(BUNDLE), "index.yaml")

# fragments assembled at runtime; no banned literal appears in this file
_f = [
    "tm" + r"\s?fo" + "rum",
    "gb" + "1042",
    "ig" + "125", "ig" + "155", "ig" + "129", "ig" + "104",
    r"\bma" + "ma\b",
    "ia" + "ade",
    r"autonomous\s+net" + "works?",
    r"\ban\s+le" + "vels?\b",
    "zero-" + "wait", "zero-" + "touch", "zero-" + "trouble",
    r"\ban" + "l\b",
]
FORBIDDEN = re.compile("|".join(_f), re.I)

errors = []

def check_text(path):
    t = open(path, encoding="utf-8").read()
    for mline in FORBIDDEN.finditer(t):
        errors.append("%s: legacy reference matched %r" % (path, mline.group(0)))

# --- catalog entry: CI-equivalent schema ---
doc = yaml.safe_load(open(CATALOG_ENTRY))
for r in ["id", "name", "domain", "version", "levels"]:
    if r not in doc:
        errors.append("catalog entry: missing %s" % r)
if len(doc.get("levels", [])) != 5:
    errors.append("catalog entry: must have exactly 5 levels")
for i, l in enumerate(doc.get("levels", [])):
    for f in ["id", "name", "score_range", "summary", "characteristics", "exit_criteria", "evidence"]:
        if f not in l:
            errors.append("catalog entry: level %d missing %s" % (i, f))

# --- index bands contiguous 0-100; level ranges + canonical_band match ---
idx = yaml.safe_load(open(INDEX))
bands = idx["catalog"]["bands"]
prev = -1
band_ranges, band_ids = [], []
for b in bands:
    lo, hi = b["range"]
    if lo != prev + 1 or hi < lo:
        errors.append("index.yaml band gap/overlap at %s" % b["id"])
    band_ranges.append(tuple(b["range"]))
    band_ids.append(b["id"])
    prev = hi
if prev != 100:
    errors.append("index.yaml bands do not cover 0-100")
for l in doc.get("levels", []):
    if tuple(l["score_range"]) not in band_ranges:
        errors.append("level %s score_range not a catalog band" % l["id"])
    if l.get("canonical_band") not in band_ids:
        errors.append("level %s canonical_band not in index.yaml" % l["id"])

# --- bundle split files exist, parse, consistent with catalog entry ---
core = yaml.safe_load(open(os.path.join(BUNDLE, "model.yaml")))
scale = yaml.safe_load(open(os.path.join(BUNDLE, "scale.yaml")))
evaluation = yaml.safe_load(open(os.path.join(BUNDLE, "evaluation.yaml")))
dimensions = yaml.safe_load(open(os.path.join(BUNDLE, "dimensions.yaml")))
if core["id"] != doc["id"]:
    errors.append("model.yaml id mismatch with catalog entry")
if scale["levels"] != doc["levels"]:
    errors.append("scale.yaml levels differ from catalog entry levels")
if evaluation["scoring"] != doc["scoring"]:
    errors.append("evaluation.yaml scoring differs from catalog entry")
if dimensions["dimensions"] != doc["dimensions"]:
    errors.append("dimensions.yaml differs from catalog entry")

# --- model content checks ---
n_crit = sum(len(s["criteria"]) for d in doc["dimensions"] for s in d["sub_dimensions"])
ids, names = [], []
for d in doc["dimensions"]:
    for s in d["sub_dimensions"]:
        for c in s["criteria"]:
            ids.append(c["id"])
            names.append(re.sub(r"\s+", " ", c["name"]).strip().lower())
if len(ids) != len(set(ids)):
    errors.append("duplicate criterion ids")
if len(names) != len(set(names)):
    errors.append("duplicate criterion names")
w = doc["scoring"]["dimension_weights"]
if abs(sum(w.values()) - 1.0) > 1e-9:
    errors.append("dimension weights do not sum to 1")
for pname, pw in doc["scoring"].get("weight_profiles", {}).items():
    if abs(sum(pw.values()) - 1.0) > 1e-9:
        errors.append("weight profile %s does not sum to 1" % pname)
    if set(pw) != set(w):
        errors.append("weight profile %s dimension keys differ from dimension_weights" % pname)
for l in doc["levels"]:
    p = l.get("progression", {})
    if set(p.get("ooda", {})) != {"Observe", "Orient", "Decide", "Act"}:
        errors.append("level %s: progression.ooda must cover Observe/Orient/Decide/Act" % l["id"])
    if not p.get("loop_driver"):
        errors.append("level %s: missing loop_driver" % l["id"])

# --- questionnaire covers every criterion exactly once ---
qp = os.path.join(BUNDLE, "assessment-questionnaire.yaml")
if os.path.exists(qp):
    qdoc = yaml.safe_load(open(qp))
    qids = [c["id"] for sec in qdoc.get("sections", []) for c in sec.get("criteria", [])]
    if sorted(qids) != sorted(ids):
        errors.append("assessment-questionnaire.yaml criteria do not match model criteria exactly")
else:
    errors.append("assessment-questionnaire.yaml missing from bundle")

# --- hygiene scan over every text file in the bundle and the catalog entry ---
for path in [CATALOG_ENTRY] + glob.glob(os.path.join(BUNDLE, "**", "*"), recursive=True):
    if os.path.isfile(path) and path.endswith((".yaml", ".md", ".py")):
        check_text(path)

if errors:
    print("FAIL:")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("OK — bundle valid: id=%s, 5 levels, %d dims / %d sub-dims / %d criteria, bands aligned, "
      "OODA ladder present, hygiene scan clean"
      % (doc["id"], len(doc["dimensions"]),
         sum(len(d["sub_dimensions"]) for d in doc["dimensions"]), n_crit))
