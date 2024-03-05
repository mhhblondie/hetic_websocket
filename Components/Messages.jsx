import { Text, View, StyleSheet } from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';

const Messages = ({ message, isCurrentUser }) => {
  const messageStyle = {
    ...styles.message,
    justifyContent: isCurrentUser ? 'flex-end' : 'flex-start',
    alignSelf: isCurrentUser ? 'flex-end' : 'flex-start',
    backgroundColor: isCurrentUser ? 'transparent' : '#3498db',
    color: 'white'
  };

  const gradientColors = isCurrentUser
    ? ['#6930C3', '#189886']
    : '#3498db';


  const messageContentStyle = {
    ...styles.messageContent,
    textAlign: isCurrentUser ? 'right' : 'left',
  };

  return (
      <LinearGradient start={{ x: 0, y: 0 }} end={{ x: 1, y: 0 }} colors={gradientColors} style={[styles.message, messageStyle]}>
      <Text style={messageContentStyle}>{message}</Text>
          </LinearGradient>
  )
}

const styles = StyleSheet.create({
  message: {
    flexDirection: 'row',
    width: 'fit-content',
    maxWidth: '60%',
    borderRadius: '20px',
    padding: 10,
    marginTop: 6,
    marginBottom: 6,
    whiteSpace: 'normal',
  },
  messageContent: {
    color: 'white',
    fontSize: '12px',
  },
})

export default Messages;