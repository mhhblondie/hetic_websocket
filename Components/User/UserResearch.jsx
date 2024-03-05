import UserCard from './UserCard'
import * as React from 'react';
import { Searchbar } from 'react-native-paper';
import { View, Text, StyleSheet } from "react-native";

const UserResearch = (Props) => {
    
    const [searchQuery, setSearchQuery] = React.useState('');

    const onChangeSearch = query => setSearchQuery(query);
    return(
        <View style={styles.container}>
            <View>
                <Searchbar
                    placeholder="Search a user"
                    onChangeText={onChangeSearch}
                    value={searchQuery}
                />
            </View>
            {Props.users.map((index,value) => (
                <View key={value}>
                    <UserCard username={index} />
                </View>
            ))}
        </View>
    );
};

const styles = StyleSheet.create({
    container: {
        padding: 10,
    },
})

export default UserResearch;