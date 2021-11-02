import axios from 'axios'

const api = axios.create({
  baseURL:
    (import.meta.env.VITE_API_BASE_URL as string) ||
    /* istanbul ignore next */ 'http://localhost:8000',
  headers: {
    Accept: 'application/json',
  },
})

export default api
