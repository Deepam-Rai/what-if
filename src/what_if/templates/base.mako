<!DOCTYPE html>
<html>

<head>
    <title>${self.title()}</title>
    <style>
        body {
            font-family: Arial;
            background: #111;
            color: #eee;
            padding: 2rem;
        }
        .choices {
            margin-top: 2rem;
        }
        a {
            color: #6cf;
            text-decoration: none;
            font-size: 1.2rem;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>

<body>
    <h1>${self.title()}</h1>
    ${self.body()}
</body>

</html>