import http from '../axios.config'

const get = async page => {
  const res = await http.get(`${page}/`).catch(err => console.log(err))
  console.log(res)
  return res.data
}

export default {
  get,
}
