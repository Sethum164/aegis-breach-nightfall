<?php
session_start();
if (!isset($_SESSION['role']) || $_SESSION['role'] !== 'admin') {
    header('Location: login.php');
    exit;
}
?>
<!DOCTYPE html>
<html>
<head><title>Admin Dashboard</title>
<style>body{font-family:Arial,sans-serif;max-width:700px;margin:40px auto;}
.box{background:#f4f6f8;border:1px solid #ccc;padding:20px;margin:15px 0;border-radius:6px;}</style>
</head>
<body>
<h2>Admin Dashboard</h2>
<p>Welcome, <?= htmlspecialchars($_SESSION['user']) ?>.</p>

<div class="box">
<h3>Stage 3 Flag</h3>
<p>AEGIS{auth_bypass_1nj3ct3d}</p>
</div>

<div class="box">
<h3>Encrypted Internal Message (Base64)</h3>
<p style="word-break:break-all;">Z3VyIHJpdnFyYXByIHN2eXIgdmYgYW56cnEgdmFwdnFyYWdfZXJjYmVnX3N2YW55LnFxIHB1cnB4IGd1ciBuaGd1IHlidCBzYmUgMDM6MTQgc3ludCB2ZiBOUlRWRnt5bmxyZWZfYnNfZ3VyX2luaHlnfQ==</p>
<p><em>Key hint: shift = the admin's lucky number: 13</em></p>
</div>
</body>
</html>
