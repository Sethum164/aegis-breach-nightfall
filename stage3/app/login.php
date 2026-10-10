<?php
session_start();
$conn = new mysqli('db', 'root', 'rootpass', 'portal');
$error = '';
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $u = $_POST['username'];
    $p = $_POST['password'];
    // Intentionally vulnerable: direct string concatenation
    $sql = "SELECT * FROM users WHERE username = '$u' AND password = '$p'";
    $result = $conn->query($sql);
    if ($result && $result->num_rows > 0) {
        $row = $result->fetch_assoc();
        $_SESSION['user'] = $row['username'];
        $_SESSION['role'] = $row['role'];
        header('Location: dashboard.php');
        exit;
    } else {
        $error = 'Invalid credentials';
    }
}
?>
<!DOCTYPE html>
<html>
<head><title>Employee Portal Login - Aeon Financial Holdings</title>
<style>body{font-family:Arial,sans-serif;max-width:400px;margin:80px auto;}
input{display:block;width:100%;padding:8px;margin:8px 0;}
button{padding:8px 20px;}
.error{color:red;}</style>
</head>
<body>
<h2>Employee Portal Login</h2>
<?php if ($error): ?><p class="error"><?= htmlspecialchars($error) ?></p><?php endif; ?>
<form method="POST">
<input type="text" name="username" placeholder="Username" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Login</button>
</form>
</body>
</html>
