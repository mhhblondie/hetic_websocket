import { Text, View, StyleSheet, Image, TouchableOpacity, FlatList } from 'react-native';
import { useRef, useEffect, useState } from 'react';
import { useNavigation } from '@react-navigation/native';
import * as ImagePicker from 'expo-image-picker';
import Icon from 'react-native-vector-icons/MaterialIcons';

const MyProfile = () => {
    const [image, setImage] = useState(null);
    const [bannerImage, setBannerImage] = useState(null);

    const navigation = useNavigation(false);
    const navigateToConvo = () => {
        navigation.navigate('Chat');
    };

    const pickImage = async () => {
        let result = await ImagePicker.launchImageLibraryAsync({
            mediaTypes: ImagePicker.MediaTypeOptions.All,
            allowsEditing: true,
            aspect: [4, 3],
            quality: 1,
        });

        console.log(result);

        if (!result.canceled) {
            setImage(result.assets[0].uri);
        }
    };

    const pickBannerImage = async () => {
        let result = await ImagePicker.launchImageLibraryAsync({
            mediaTypes: ImagePicker.MediaTypeOptions.All,
            allowsEditing: true,
            aspect: [16, 9],
            quality: 1,
        });

        console.log(result);

        if (!result.canceled) {
            setBannerImage(result.assets[0].uri);
        }
    };
    return (
        <View style={styles.container}>
            <TouchableOpacity style={styles.banner} activeOpacity={0.9} onPress={pickBannerImage}>
                <Image source={{ uri: bannerImage, width: '100%', height: 115 }} />
            </TouchableOpacity>
            <Icon name="close" size={16} color="white" onPress={navigateToConvo} style={{position: 'absolute', marginTop: 20, marginLeft: 20, padding: 6, borderRadius: '50%', backgroundColor: 'black'}} />
            <View style={styles.userInfo}>
                <TouchableOpacity style={styles.profilePicture} activeOpacity={0.9} onPress={pickImage}>
                    <Image source={{ uri: image }} style={styles.profilePicture} />
                </TouchableOpacity>
                <Text style={styles.username}>Username</Text>
            </View>
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
    },
    banner: {
        flex: 1,
        width: '100%',
        maxHeight: 115,
        backgroundColor: '#6930C3',
    },
    userInfo: {
        display: 'flex',
        flexDirection: 'row',
        justifyContent: 'center',
        alignItems: 'center',
        position: 'absolute',
        marginTop: 100,
        marginLeft: 20
    },
    profilePicture: {
        width: 90,
        height: 90,
        borderRadius: '50%',
        backgroundColor: '#189886'
    },
    username: {
        color: 'white',
        fontSize: '24px',
        marginLeft: 20
    },
})

export default MyProfile;