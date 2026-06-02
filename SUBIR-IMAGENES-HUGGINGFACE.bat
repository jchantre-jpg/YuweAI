@echo off
chcp 65001 >nul
cd /d "%~dp0.."
echo ========================================
echo  Subir imagenes a Hugging Face (GRATIS, sin tarjeta)
echo  Dataset: Juliana08/yuwe-dict-images
echo ========================================
echo.

if "%HF_TOKEN%"=="" (
  echo Define tu token de Hugging Face:
  echo   set HF_TOKEN=hf_xxxxxxxx
  echo.
  echo Crear en: https://huggingface.co/settings/tokens  ^(permiso Write^)
  pause
  exit /b 1
)

set HF_HUB_DISABLE_XET=1
pip install huggingface_hub -q
python scripts/upload_corpus_hf_dataset.py
if errorlevel 1 pause & exit /b 1

echo.
echo En Render - Environment Variables:
echo   SOLO_IMG_CDN_BASE=https://huggingface.co/datasets/Juliana08/yuwe-dict-images/resolve/main
echo   ^(borra FIREBASE_STORAGE_BUCKET si lo pusiste^)
echo.
pause
