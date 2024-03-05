import React from 'react';
import { createStackNavigator } from '@react-navigation/stack';
import MessagesPage from '../Pages/MessagesPage';
import NewConvoPage from '../Pages/NewMessage';
import MyProfile from '../Pages/Profile';

const Stack = createStackNavigator();

const StackNavigator = () => {
    return (
        <Stack.Navigator>
            <Stack.Screen name="New convo" component={NewConvoPage} options={{ headerShown: false, unmountOnBlur: true }} />
            <Stack.Screen name="Chat" component={MessagesPage} options={{ headerShown: false, unmountOnBlur: true }} />
            <Stack.Screen name="My profile" component={MyProfile} options={{ headerShown: false, unmountOnBlur: true }} />
        </Stack.Navigator>
    );
};

export default StackNavigator;