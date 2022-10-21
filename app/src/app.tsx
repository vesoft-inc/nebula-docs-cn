import { createRoot } from 'react-dom/client'
import SearchDialog from './components/SearchDialog'

const container = document.getElementById('doc-search')
const root = createRoot(container)

root.render(<SearchDialog></SearchDialog>)
