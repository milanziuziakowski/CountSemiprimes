# Download example papers used in SUPER_DISCOVERY
if (-not (Test-Path '.\\resources')) { New-Item -ItemType Directory -Path '.\\resources' | Out-Null }
Invoke-WebRequest -Uri 'https://arxiv.org/pdf/2405.20748v1' -OutFile '.\\resources\\OpenTensor-2405.20748v1.pdf' -UseBasicParsing
Write-Output 'Downloaded OpenTensor to resources\\OpenTensor-2405.20748v1.pdf'
# Check license before redistribution
