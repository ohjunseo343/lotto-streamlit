<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>Random Number</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 80px;
        }
        #number {
            font-size: 50px;
            margin-top: 20px;
            font-weight: bold;
        }
        button {
            padding: 12px 25px;
            font-size: 18px;
            cursor: pointer;
        }
    </style>
</head>
<body>

    <h2>1~20 랜덤 숫자 뽑기</h2>

    <button onclick="pickNumber()">숫자 뽑기</button>

    <div id="number"></div>

    <script>
        function pickNumber() {
            const num = Math.floor(Math.random() * 20) + 1;
            document.getElementById("number").textContent = num;
        }
    </script>

</body>
</html>
