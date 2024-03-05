import React from "react";
import { View, Text } from "react-native";
const UserCard = (props) => {
    return(
        <View style={Styles.UserCard}>
            <View style={Styles.Profil}></View>
            <Text style={Styles.userList} >{props.username}</Text>
        </View>
    )
}
const Styles = {
    UserCard:{
        padding: 10,
        display:'flex',
        flexDirection:'row',
        alignItems: 'center',
    },
    Profil:{
        height:30,
        width:30,
        borderRadius:50,
        backgroundColor:'#6930C3',
        margin:10
    },
    userList: {
        color: 'white'
    }
}
export default UserCard;