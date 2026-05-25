# Crea solo-img-ia.tar.gz en la raiz del repo YuweAI (hermano de corpus/ y web/).
# Uso: desde la raiz YuweAI:  powershell -ExecutionPolicy Bypass -File scripts/make_solo_img_tar_for_render.ps1
$ErrorActionPreference = "Stop"
$RepoRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$SoloDir = Join-Path $RepoRoot "corpus\generadas-img-ia-solo"
$OutFile = Join-Path $RepoRoot "solo-img-ia.tar.gz"

if (-not (Test-Path $SoloDir)) {
    Write-Error "No existe: $SoloDir"
}

$pngCount = (Get-ChildItem -Path $SoloDir -Recurse -Filter "*.png" -ErrorAction SilentlyContinue | Measure-Object).Count
Write-Host "PNG encontrados: $pngCount"
if ($pngCount -lt 1) {
    Write-Error "No hay PNG en $SoloDir. Sincroniza OneDrive o copia las imagenes antes de empaquetar."
}

if (Test-Path $OutFile) {
    Remove-Item -Force $OutFile
}

Push-Location $RepoRoot
try {
    # Contenido en la raiz del .tar (recomendado). Compatible con el Dockerfile en Render.
    & tar -czvf $OutFile -C (Join-Path $RepoRoot "corpus\generadas-img-ia-solo") .
    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
} finally {
    Pop-Location
}

$item = Get-Item $OutFile
Write-Host ""
Write-Host "Listo: $($item.FullName)"
Write-Host "Tamano: $([math]::Round($item.Length / 1GB, 2)) GB"
Write-Host ""
Write-Host "Siguiente paso (Render):"
Write-Host "  1) Sube este .tar.gz a un sitio con URL directa (release de GitHub, bucket S3/R2, Hugging Face file)."
Write-Host "  2) En Render -> yuweai-avi-api -> Environment -> SOLO_IMG_TARBALL_URL = esa URL HTTPS"
Write-Host "  3) Manual Deploy (o push) para reconstruir la imagen Docker."
Write-Host ""
Write-Host "GitHub (tras: gh auth login):"
Write-Host "  gh release create solo-img-ia-v1 $OutFile --repo jchantre-jpg/YuweAI --title \"Solo corpus images\" --notes \"Para SOLO_IMG_TARBALL_URL en Render\""
