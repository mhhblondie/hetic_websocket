import 'react-native-gesture-handler';
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, View } from 'react-native';

import { NavigationContainer } from '@react-navigation/native';
import StackNavigator from './navigation/StackNavigation';

export default function App() {
  return (
    <NavigationContainer style={styles.container}>
      <StackNavigator />
    </NavigationContainer>
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
})