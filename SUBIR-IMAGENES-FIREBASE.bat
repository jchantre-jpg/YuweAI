@echo off
chcp 65001 >nul
cd /d "%~dp0.."
echo ========================================
echo  Subir imagenes del diccionario a Firebase Storage
echo  Proyecto: yuwe-ai (plan Spark = gratis con limites)
echo ========================================
echo.

if "%GOOGLE_APPLICATION_CREDENTIALS%"=="" (
  echo ERROR: Define la clave JSON de Firebase:
  echo   set GOOGLE_APPLICATION_CREDENTIALS=C:\ruta\yuwe-ai-firebase-adminsdk.json
  echo.
  echo Firebase Console - yuwe-ai - Configuracion - Cuentas de servicio - Generar clave
  pause
  exit /b 1
)

pip install google-cloud-storage -q
python scripts/upload_corpus_firebase_storage.py --workers 10
if errorlevel 1 pause & exit /b 1

echo.
echo Desplegando reglas de Storage (lectura publica corpus-img/)...
cd web\frontend
call npx firebase deploy --only storage --non-interactive
cd ..\..

echo.
echo Anade en Render - Environment:
echo   FIREBASE_STORAGE_BUCKET=yuwe-ai.firebasestorage.app
echo   FIREBASE_STORAGE_PREFIX=corpus-img
echo.
pause
