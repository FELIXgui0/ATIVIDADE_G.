import React from 'react'; 
import { StyleSheet, Text, View, Image, StatusBar } from 'react-native';

export default function App() {
  return (
    <View style={styles.container}>
      <StatusBar barStyle="light-content" backgroundColor="#000000" />
      <View style={styles.card}>
        <Image
          source={{ uri: 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.istockphoto.com%2Fbr%2Ffotos%2Fbasquete&psig=AOvVaw2f_G0yahxWj0yYW22yOYJO&ust=1744121279176000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCKChgp6MxowDFQAAAAAdAAAAABAE' }} 
          style={styles.profileImage}
        />
        <Text style={styles.name}>Guilherme Rafael</Text> {/* Novo nome */}
        <Text style={styles.phrase}>“Adoro jogar basquete e treinar.”</Text> {/* Nova frase */}
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#000000', 
    alignItems: 'center',
    justifyContent: 'center',
    padding: 16,
  },
  card: {
    backgroundColor: '#333333',
    borderRadius: 20,
    padding: 24,
    alignItems: 'center',
    shadowColor: '#000',
    shadowOpacity: 0.3,
    shadowRadius: 10,
    elevation: 10,
    width: '100%',
    maxWidth: 320,
  },
  profileImage: {
    width: 120,
    height: 120,
    borderRadius: 60,
    marginBottom: 16,
    borderWidth: 2,
    borderColor: '#00d1ff',
  },
  name: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#ffffff',
    marginBottom: 8,
  },
  phrase: {
    fontSize: 16,
    fontStyle: 'italic',
    color: '#cccccc',
    textAlign: 'center',
  },
});