import { useState } from 'react';
import { View, TextInput, StyleSheet, TouchableOpacity } from 'react-native';
import Icon from 'react-native-vector-icons/MaterialIcons';

const InputBar = ({ onSendMessage }) => {
  const [newMessage, setNewMessage] = useState('');

  const sendMessage = () => {
    if (newMessage.trim() !== '') {
      onSendMessage(newMessage);
      setNewMessage('');
    }
  };

  return (
    <View style={styles.container}>
      {/* <TouchableOpacity style={styles.moreActionButton} activeOpacity={0.7}></TouchableOpacity> */}
      <TextInput
        style={styles.myInput}
        multiline={true}
        placeholder="Write a message..." 
        value={newMessage}
        onChangeText={(text) => setNewMessage(text)}
      />
      <TouchableOpacity style={styles.sendButton} activeOpacity={0.7} onPress={sendMessage}>
        <Icon name="send" size={15} color="white" />
      </TouchableOpacity>
    </View>
  )
}

const styles = StyleSheet.create({
  container: {
    width: '100%',
    display: 'flex',
    jusrifyContent: 'center',
    flexDirection: 'row',
    alignItems: 'center',
  },
  myInput: {
    width: '100%',
    height: '35px',
    maxHeight: '100%',
    padding: 8,
    marginLeft: 8,
    marginRight: 8,
    borderWidth: 1,
    borderRadius: 20,
    borderColor: 'grey',
    backgroundColor: '#091C39',
    color: 'white',
    fontSize: '12px',
  },
  sendButton: {
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    maxWidth: '10%',
    width: '30px',
    height: '30px',
    borderRadius: '50%',
    backgroundColor: '#6930C3'
  },
  moreActionButton: {
    maxWidth: '10%',
    width: '30px',
    height: '30px',
    borderRadius: '50%',
    backgroundColor: '#6930C3'
  }
})

export default InputBar;