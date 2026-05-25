import { Component, StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import { initFirebase } from './firebase.js'

initFirebase()

class RootErrorBoundary extends Component {
  constructor(props) {
    super(props)
    this.state = { error: null }
  }

  static getDerivedStateFromError(error) {
    return { error }
  }

  render() {
    if (this.state.error) {
      return (
        <main style={{ padding: '24px', fontFamily: 'Inter, sans-serif', color: '#1d271e' }}>
          <h1 style={{ margin: 0, fontSize: '1.4rem' }}>La app tuvo un error inesperado</h1>
          <p style={{ marginTop: '0.65rem', color: '#5c6558' }}>
            Recarga la pagina. Si vuelve a pasar, copia este mensaje y me lo envias.
          </p>
          <pre
            style={{
              marginTop: '0.85rem',
              padding: '0.75rem',
              borderRadius: '10px',
              background: '#f5f3eb',
              border: '1px solid #dcd2bd',
              whiteSpace: 'pre-wrap',
            }}
          >
            {String(this.state.error?.stack || this.state.error?.message || this.state.error)}
          </pre>
          <button
            type="button"
            onClick={() => window.location.reload()}
            style={{ marginTop: '0.85rem', padding: '0.5rem 0.85rem', borderRadius: '999px', cursor: 'pointer' }}
          >
            Recargar
          </button>
        </main>
      )
    }
    return this.props.children
  }
}

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <RootErrorBoundary>
      <App />
    </RootErrorBoundary>
  </StrictMode>,
)
