<?php


$a = isset($_GET['a']) ? $_GET['a'] : '';
$b = isset($_GET['b']) ? $_GET['b'] : '';
$c = isset($_GET['c']) ? $_GET['c'] : '';

function esc($v) { return escapeshellarg($v); }

$python = '/usr/bin/python3'; 
$script = __DIR__ . DIRECTORY_SEPARATOR . 'calculate.py';

$output = '';
if ($a !== '' && $b !== '' && $c !== '') {
    $cmd = $python . ' ' . esc($script) . ' ' . esc("a=$a") . ' ' . esc("b=$b") . ' ' . esc("c=$c");
    $output = shell_exec($cmd);
}
?>
<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>Assignment 2</title>
<style>
body{font-family:Arial,sans-serif;margin:2rem}
.card{border:1px solid #ddd;padding:1rem;border-radius:8px;max-width:900px}
label{display:block;margin:.5rem 0} input,button{padding:.5rem}
.muted{color:#666}
</style></head><body>
<h1>Assignment 2</h1>

<div class="card">
  <form method="get" action="">
    <label>a: <input type="number" step="any" name="a" value="<?=htmlspecialchars($a)?>" required></label>
    <label>b: <input type="number" step="any" name="b" value="<?=htmlspecialchars($b)?>" required></label>
    <label>c: <input type="number" step="any" name="c" value="<?=htmlspecialchars($c)?>" required></label>
    <button type="submit">Calculate</button>
  </form>
</div>

<div class="card" style="margin-top:1rem">
  <h2>Output</h2>
  <?php
    if ($output) { echo $output; }
    else { echo "<p class='muted'>Enter values and submit to see the result.</p>"; }
  ?>
</div>
</body></html>