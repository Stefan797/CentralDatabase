<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="icon" type="image/png" href="/images/favIcon.png"/>
        <title>CentralDatabase</title>
        <link rel="stylesheet" href="/test.css">
        <style>
            .main {
                height: 100vh;
                width: 100vw;
            }
        </style>

        @vite('resources/js/app.js')
        @vite('resources/css/app.css')
    </head>
    <body>
        <div id="app" class="main">
            {{ $slot }}
        </div>
    </body>
</html>