import { useCallback, useEffect, useMemo, useRef, useState } from 'react'
import {
  ActivityIndicator,
  BackHandler,
  Image,
  Platform,
  Pressable,
  StatusBar,
  StyleSheet,
  Text,
  View,
} from 'react-native'
import { StatusBar as ExpoStatusBar } from 'expo-status-bar'
import Constants from 'expo-constants'
import { SafeAreaProvider, SafeAreaView } from 'react-native-safe-area-context'
import { WebView } from 'react-native-webview'

const BRAND_ASSETS = {
  logo: require('./assets/imagenes/Logo.png'),
  welcome: require('./assets/imagenes/bienvenida.png'),
  chat: require('./assets/imagenes/Logo chat avi.png'),
}

const INJECTION_FLAG = `
  (function(){ try { window.__AVI_EXPO_SHELL__ = true; } catch(e) {} })();
  true;
`

function resolveWebUrl() {
  const envUrl = process.env.EXPO_PUBLIC_WEB_APP_URL
  const extra = Constants?.expoConfig?.extra || {}
  if (envUrl) return envUrl
  if (extra.webAppUrl) return extra.webAppUrl
  if (extra.apiBase && typeof extra.apiBase === 'string') return extra.apiBase
  return 'http://192.168.43.243:8090'
}

export default function App() {
  const webAppUrl = useMemo(resolveWebUrl, [])
  const webViewRef = useRef(null)
  const [loading, setLoading] = useState(true)
  const [failed, setFailed] = useState(false)
  const [reloadKey, setReloadKey] = useState(0)
  const [canGoBack, setCanGoBack] = useState(false)

  const onNavStateChange = useCallback((navState) => {
    setCanGoBack(Boolean(navState?.canGoBack))
  }, [])

  useEffect(() => {
    if (Platform.OS !== 'android') return undefined
    const sub = BackHandler.addEventListener('hardwareBackPress', () => {
      if (failed) return false
      if (canGoBack && webViewRef.current) {
        webViewRef.current.goBack()
        return true
      }
      return false
    })
    return () => sub.remove()
  }, [canGoBack, failed])

  return (
    <SafeAreaProvider>
      <SafeAreaView style={styles.safe} edges={['top']}>
        <View style={styles.root}>
          <ExpoStatusBar style="dark" />
          <StatusBar barStyle="dark-content" />
          {failed ? (
            <View style={styles.errorWrap}>
              <Image source={BRAND_ASSETS.logo} style={styles.errorLogo} resizeMode="contain" />
              <Text style={styles.errorTitle}>No se pudo abrir la app completa</Text>
              <Text style={styles.errorBody}>
                La app movil carga la misma interfaz que la web (todas las pantallas y roles). Comprueba que el
                servidor este en marcha y la URL sea alcanzable desde el telefono:
              </Text>
              <Text style={styles.url}>{webAppUrl}</Text>
              <Pressable
                style={styles.retryBtn}
                onPress={() => {
                  setFailed(false)
                  setReloadKey((v) => v + 1)
                }}
              >
                <Text style={styles.retryTxt}>Reintentar</Text>
              </Pressable>
            </View>
          ) : (
            <>
              <WebView
                ref={webViewRef}
                key={reloadKey}
                source={{ uri: webAppUrl }}
                style={styles.webview}
                javaScriptEnabled
                domStorageEnabled
                sharedCookiesEnabled
                thirdPartyCookiesEnabled
                allowsInlineMediaPlayback
                mediaPlaybackRequiresUserAction={false}
                mixedContentMode="always"
                allowsBackForwardNavigationGestures
                allowFileAccess
                allowUniversalAccessFromFileURLs={false}
                geolocationEnabled
                setSupportMultipleWindows={false}
                injectedJavaScriptBeforeContentLoaded={INJECTION_FLAG}
                onLoadStart={() => setLoading(true)}
                onLoadEnd={() => setLoading(false)}
                onNavigationStateChange={onNavStateChange}
                onError={() => {
                  setLoading(false)
                  setFailed(true)
                }}
              />
              {loading ? (
                <View style={styles.loader}>
                  <View style={styles.loaderBrand}>
                    <Image source={BRAND_ASSETS.welcome} style={styles.loaderMascot} resizeMode="contain" />
                    <Image source={BRAND_ASSETS.chat} style={styles.loaderChatLogo} resizeMode="contain" />
                  </View>
                  <ActivityIndicator size="large" color="#7a4a16" />
                  <Text style={styles.loaderText}>Cargando AVI completo…</Text>
                </View>
              ) : null}
            </>
          )}
        </View>
      </SafeAreaView>
    </SafeAreaProvider>
  )
}

const styles = StyleSheet.create({
  safe: {
    flex: 1,
    backgroundColor: '#f7f1e8',
  },
  root: {
    flex: 1,
    backgroundColor: '#f7f1e8',
  },
  webview: {
    flex: 1,
    backgroundColor: '#fff',
  },
  loader: {
    position: 'absolute',
    inset: 0,
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: 'rgba(247, 241, 232, 0.9)',
    gap: 10,
  },
  loaderBrand: {
    alignItems: 'center',
    justifyContent: 'center',
    gap: 8,
  },
  loaderMascot: {
    width: 180,
    height: 140,
  },
  loaderChatLogo: {
    width: 54,
    height: 54,
  },
  loaderText: {
    color: '#6b4a22',
    fontWeight: '700',
  },
  errorWrap: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    padding: 24,
    gap: 12,
  },
  errorTitle: {
    fontSize: 20,
    fontWeight: '800',
    color: '#6d3f11',
    textAlign: 'center',
  },
  errorLogo: {
    width: 120,
    height: 120,
    marginBottom: 6,
  },
  errorBody: {
    textAlign: 'center',
    color: '#664e2f',
  },
  url: {
    textAlign: 'center',
    color: '#1f4b7a',
    fontWeight: '700',
  },
  retryBtn: {
    marginTop: 6,
    backgroundColor: '#7a4a16',
    borderRadius: 12,
    paddingVertical: 11,
    paddingHorizontal: 18,
  },
  retryTxt: {
    color: '#fff',
    fontWeight: '800',
  },
})
