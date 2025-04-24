
$DIR = Split-Path -Parent $MyInvocation.MyCommand.Path

if (-Not (Test-Path "$DIR\data")) {
    New-Item -ItemType Directory -Path "$DIR\data"
} else {
    Write-Host "'data' directory already exists."
}

Invoke-WebRequest -Uri "https://drive.google.com/uc?id=1qadBd7lgpediafCpL_yedGjQPk-FLK-W" -OutFile "$DIR\data\traffic_analysis.mov"

Invoke-WebRequest -Uri "https://drive.google.com/uc?id=1y-IfToCjRXa3ZdC1JpnKRopC7mcQW-5z" -OutFile "$DIR\data\traffic_analysis.pt"