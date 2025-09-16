import os, sys, math
from urllib.parse import parse_qs

def parse_inputs():
    params = {}
  
    for arg in sys.argv[1:]:
        if "=" in arg:
            k, v = arg.split("=", 1)
            params[k.strip()] = v.strip()
   
    if not params:
        qs = os.environ.get("QUERY_STRING", "")
        if qs:
            for k, v in parse_qs(qs).items():
                if v:
                    params[k] = v[0]
    try:
        a = float(params.get("a", ""))
        b = float(params.get("b", ""))
        c = float(params.get("c", ""))
    except Exception:
        raise ValueError("Please supply numeric a, b, c")
    if a == 0:
        raise ZeroDivisionError("'a' cannot be 0 (division by zero).")
    return a, b, c

def html(body):
    return f"""Content-Type: text/html

<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><title>Assignment 2 Result</title>
<style>
body{{font-family:Arial,sans-serif;margin:2rem}} .card{{border:1px solid #ddd;padding:1rem;border-radius:8px;max-width:800px}}
.muted{{color:#666}}
</style></head><body>
<h1>Assignment 2 — Calculation</h1>
<div class="card">{body}</div>
</body></html>"""

def main():
    try:
        a,b,c = parse_inputs()
        c3 = c**3
        s  = c3**0.5
        d  = s / a
        m  = d * 10
        result = m + b
        body = f"""
        <h2>Inputs</h2>
        <ul><li>a = {a}</li><li>b = {b}</li><li>c = {c}</li></ul>
        <h2>Steps</h2>
        <ol>
          <li>c^3 = {c3}</li>
          <li>√(c^3) = {s}</li>
          <li>Divide by a: {s} / {a} = {d}</li>
          <li>Multiply by 10: {d} * 10 = {m}</li>
          <li>Add b: {m} + {b} = <strong>{result}</strong></li>
        </ol>
        <h2>Final Result</h2><p><strong>{result}</strong></p>
        <p class="muted">Tip: try <code>?a=3&b=5&c=2</code></p>
        """
        print(html(body))
    except Exception as e:
        print(html(f"<h2>Error</h2><p>{e}</p>"))

if __name__ == "__main__":
    main()