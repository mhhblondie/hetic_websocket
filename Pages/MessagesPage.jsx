import { Text, View, StyleSheet, TouchableOpacity, FlatList } from 'react-native';
import { useRef, useEffect, useState } from 'react';

import Messages from '../Components/Messages';
import InputBar from '../Components/InputBar';
import { useNavigation } from '@react-navigation/native';

const MessagesPage = () => {
  const [messages, setMessages] = useState([]);
  const messagesContainer = useRef(null);
  const currentUserId = "1";

  const sendMessage = (message) => {
    setMessages([...messages, { id: messages.length + 1, text: message, userId: currentUserId }]);
  };

  const scrollToBottom = () => {
    if (messagesContainer.current) {
      messagesContainer.current.scrollToEnd({ animated: true });
    }
  };
  useEffect(() => {
    scrollToBottom();
  }, []);

  const navigation = useNavigation(false);
  const navigateToNewConvo = () => {
    navigation.navigate('New convo');
  };
  const navigateToMyProfile = () => {
    navigation.navigate('My profile');
  };

  return (
    <View style={styles.container}>
      <View style={styles.header}>
        <View style={styles.header2}>
          <Text style={styles.title}>Messages</Text>
        </View>
        <TouchableOpacity style={styles.myProfil} onPress={navigateToMyProfile}></TouchableOpacity>
      </View>
      <View style={{
        width: '100%',
        flexDirection: 'row',
        alignItems: 'center'
      }}>
        <TouchableOpacity style={styles.newConvo}>
          <Text style={{ display: 'flex', justifyContent: 'center', color: 'white', fontSize: '30px' }} onPress={navigateToNewConvo}>+</Text>
        </TouchableOpacity>
        <View style={styles.verticalLine}></View>
        <TouchableOpacity style={styles.isConvoActive}>
        </TouchableOpacity>
      </View>
      <View style={styles.messageContainer}>
        <FlatList
        ref={messagesContainer} onContentSizeChange={() => scrollToBottom()}
        data={messages}
        keyExtractor={(item) => item.id.toString()}
          renderItem={({ item }) => <Messages message={item.text} isCurrentUser={item.userId === currentUserId} />}
      />
      </View>
      <InputBar onSendMessage={sendMessage} />
    </View>
  )
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    width: '100%',
    height: '100%',
    // position: 'fixed',
    backgroundColor: '#091C39',
    padding: 15,
    position: 'absolute',
  },
  header: {
    flex: 1,
    width: '100%',
    maxHeight: '15%',
    color: 'white',
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
  },
  header2: {
    flex: 1,
    display: 'flex',
    flexDirection: 'row',
    justifyContent: 'center',
    alignItems: 'center',
  },
  myProfil: {
    display: 'flex',
    alignItems: 'end',
    justifyContent: 'center',
    borderRadius: '50%',
    width: '30px',
    height: '30px',
    backgroundColor: '#189886',
    margin: 6,
  },
  title: {
    color: 'white',
    fontSize: '24px',
  },
  newConvo: {
    width: '45px',
    height: '45px',
    borderRadius: '15px',
    borderWidth: 1,
    borderColor: 'white',
  },
  verticalLine: {
    height: '80%',
    width: 1,
    margin: 10,
    backgroundColor: '#fff',
  },
  contact: {
    width: '45px',
    height: '45px',
    borderRadius: '15px',
    borderWidth: 1,
    borderColor: 'white',
    marginRight: 10,
  },
  isConvoActive: {
    width: '45px',
    height: '45px',
    borderRadius: '50%',
    borderWidth: 1,
    borderColor: '#189886',
  },
  messageContainer: {
    flex: 1,
    width: '100%',
    padding: 10,
    marginTop: 10,
    marginBottom: 10,
    borderRadius: '10px',
    boxShadow: 'inset 0px 0px 5px 0 rgba(255, 255, 255, 0.2)',
  },
})

export default MessagesPage;