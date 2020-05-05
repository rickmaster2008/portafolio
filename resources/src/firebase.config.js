import firebase from 'firebase/app'
import 'firebase/database'
import 'firebase/auth'

const config = {
  apiKey: 'AIzaSyAcPy585PCtJdaleQ9uvnQ29EtebeHHUjo',
  authDomain: 'cotillo-1daca.firebaseapp.com',
  databaseURL: 'https://cotillo-1daca.firebaseio.com',
  projectId: 'cotillo-1daca',
  storageBucket: 'cotillo-1daca.appspot.com',
  messagingSenderId: '561187008402',
  appId: '1:561187008402:web:738ed65f73a22fc6a69b4b',
}

firebase.initializeApp(config)
export const db = firebase.database()
export const auth = firebase.auth()
