import React from 'react';
import { Button, Text, View, StyleSheet, Image } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';

const Stack = createStackNavigator();

function HomeScreen({ navigation }) {
  return (
    <View style={styles.homeContainer}>
      <Text style={styles.homeText}>Bem-vindo ao Meu App!</Text>
      <Text style={styles.homeSubText}>Explore duas telas incríveis e conheça mais sobre você!</Text>
      <Button
        title="Ir para a Tela de Perfil"
        onPress={() => navigation.navigate('Perfil')}
        color="#ff6347" // Cor do botão mais vibrante
      />
    </View>
  );
}

function PerfilScreen() {
  return (
    <View style={styles.perfilContainer}>
      <Image
        source={{ uri: 'https://randomuser.me/api/portraits/men/1.jpg' }} // Substituí o link da imagem por um link válido
        style={styles.profileImage}
      />
      <Text style={styles.perfilText}>Olá, eu sou o Guilherme Rafael!</Text>
      <Text style={styles.perfilBio}>Desenvolvedor apaixonado por tecnologia, música e viagens. 🖥️🎶✈️</Text>
      <Text style={styles.perfilQuote}>“A vida é feita de momentos, e estou pronto para aproveitar cada um deles!”</Text>
    </View>
  );
}

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Home">
        <Stack.Screen name="Home" component={HomeScreen} />
        <Stack.Screen name="Perfil" component={PerfilScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

// Estilos
const styles = StyleSheet.create({
  // Estilos para a Tela Inicial (Home)
  homeContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#fffae1', // Fundo amarelo suave
    padding: 20,
  },
  homeText: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#333', // Cor escura para o texto principal
    marginBottom: 10,
  },
  homeSubText: {
    fontSize: 18,
    color: '#666', // Cor mais suave para o texto secundário
    marginBottom: 20,
    textAlign: 'center',
  },

  // Estilos para a Tela de Perfil (Perfil)
  perfilContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#1e1e1e', // Fundo escuro para a tela de perfil
    padding: 20,
  },
  profileImage: {
    width: 150,
    height: 150,
    borderRadius: 75,
    marginBottom: 20,
    borderWidth: 3,
    borderColor: '#ff6347', // Borda da imagem com cor vibrante
  },
  perfilText: {
    fontSize: 28,
    fontWeight: 'bold',
    color: '#ffffff', // Texto branco
    marginBottom: 10,
  },
  perfilBio: {
    fontSize: 18,
    color: '#cccccc', // Texto em cinza claro
    textAlign: 'center',
    marginBottom: 10,
  },
  perfilQuote: {
    fontSize: 16,
    color: '#ffffff', // Citação em branco para destacá-la
    fontStyle: 'italic',
    textAlign: 'center',
  },
});
