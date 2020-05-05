<template>
  <div>
    <div v-if="bubble" class="speech-bubble">
      <span>hey! como estás?</span>
    </div>
    <beautiful-chat
      class="chat"
      :participants="participants"
      :onMessageWasSent="onMessageWasSent"
      :messageList="messageList"
      :newMessagesCount="newMessagesCount"
      :isOpen="isChatOpen"
      :close="closeChat"
      :icons="icons"
      :open="openChat"
      :showEmoji="false"
      :showFile="false"
      :showTypingIndicator="showTypingIndicator"
      :colors="colors"
      :alwaysScrollToBottom="alwaysScrollToBottom"
      :messageStyling="messageStyling"
    />
  </div>
</template>

<script>
import CloseIcon from 'vue-beautiful-chat/src/assets/close-icon.png'
import FileIcon from 'vue-beautiful-chat/src/assets/file.svg'
import CloseIconSvg from 'vue-beautiful-chat/src/assets/close.svg'
import Chat from '@/assets/img/icons/chat.svg'
import { db, auth } from '@/firebase.config'
export default {
  created() {
    auth.onAuthStateChanged(user => {
      if (user) {
        this.uid = user.uid
        this.$rtdbBind('messageList', db.ref(`messages/${user.uid}`))
      } else {
        console.log('logged out')
      }
    })

    auth.signInAnonymously().catch(function() {
      // var errorCode = error.code
      // var errorMessage = error.message
    })
  },
  data() {
    return {
      bubble: false,
      uid: null,
      icons: {
        open: {
          img: Chat,
          name: 'default',
        },
        close: {
          img: CloseIcon,
          name: 'default',
        },
        file: {
          img: FileIcon,
          name: 'default',
        },
        closeSvg: {
          img: CloseIconSvg,
          name: 'default',
        },
      },
      participants: [
        {
          id: 'user2',
          name: 'Ricardo',
          imageUrl:
            'https://avatars3.githubusercontent.com/u/37018832?s=200&v=4',
        },
      ], // the list of all the participant of the conversation. `name` is the user name, `id` is used to establish the author of a message, `imageUrl` is supposed to be the user avatar.
      messageList: [], // the list of the messages to show, can be paginated and adjusted dynamically
      newMessagesCount: 0,
      isChatOpen: false, // to determine whether the chat window should be open or closed
      showTypingIndicator: '', // when set to a value matching the participant.id it shows the typing indicator for the specific user
      colors: {
        header: {
          bg: '#095a70',
          text: '#ffffff',
        },
        launcher: {
          bg: '#206275',
          text: '#ffffff',
        },
        messageList: {
          bg: '#ffffff',
        },
        sentMessage: {
          bg: '#4dacbc',
          text: '#ffffff',
        },
        receivedMessage: {
          bg: '#eaeaea',
          text: '#222222',
        },
        userInput: {
          bg: '#f4f7f9',
          text: '#565867',
        },
      }, // specifies the color scheme for the component
      alwaysScrollToBottom: true, // when set to true always scrolls the chat to the bottom when new events are in (new message, user starts typing...)
      messageStyling: true, // enables *bold* /emph/ _underline_ and such (more info at github.com/mattezza/msgdown)
    }
  },
  firebase: {},
  methods: {
    sendMessage(text) {
      console.log(text)
      // if (text.length > 0) {
      //   this.newMessagesCount = this.isChatOpen
      //     ? this.newMessagesCount
      //     : this.newMessagesCount + 1
      //   this.onMessageWasSent({
      //     author: 'support',
      //     type: 'text',
      //     data: { text },
      //   })
      // }
    },
    onMessageWasSent(message) {
      // called when the user sends a message
      db.ref(`messages/${this.uid}`)
        .push({
          type: 'text',
          author: 'me',
          data: message.data,
        })
        .then(res => console.log(res))
        .catch(err => console.log(err))
    },
    openChat() {
      // called when the user clicks on the fab button to open the chat
      this.isChatOpen = true
      this.newMessagesCount = 0
    },
    closeChat() {
      // called when the user clicks on the botton to close the chat
      this.isChatOpen = false
    },
    handleScrollToTop() {
      // called when the user scrolls message list to top
      // leverage pagination for loading another page of messages
    },
    handleOnType() {
      console.log('Emit typing event')
    },
    editMessage(message) {
      const m = this.messageList.find(m => m.id === message.id)
      m.isEdited = true
      m.data.text = message.data.text
    },
  },
}
</script>

<style scoped>
.speech-bubble {
  color: white;
  position: relative;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 0.4em;
  padding: 1em;
  margin-bottom: 1.2em;
}

.speech-bubble:after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 10%;
  width: 0;
  height: 0;
  border: 0.719em solid transparent;
  border-top-color: rgba(255, 255, 255, 0.2);
  border-bottom: 0;
  border-left: 0;
  margin-left: -0.359em;
  margin-bottom: -0.719em;
}
</style>
