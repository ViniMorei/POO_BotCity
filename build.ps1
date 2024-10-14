$exclude = @("venv", "produtoPOO.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "produtoPOO.zip" -Force