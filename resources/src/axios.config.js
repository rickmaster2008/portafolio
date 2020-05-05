import axios from 'axios'
import csrftoken from './csrf.config'

export default axios.create({
  baseURL: '/api/v2',
  timeout: 1000,
  headers: {
    'Content-Type': 'application/json',
    'X-CSRFToken': csrftoken
  },
})
