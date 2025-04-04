import React, { useState } from 'react';
import { View, Text, TextInput, TouchableOpacity, StyleSheet } from 'react-native';

const App = () => {
  const [nome, setNome] = useState('');
  const [saudacao, setSaudacao] = useState('');

  const obterSaudacao = () => {
    const hora = new Date().getHours();
    if (hora < 12) return 'Bom dia';
    if (hora < 18) return 'Boa tarde';
    return 'Boa noite';
  };

  const atualizarSaudacao = () => {
    if (nome.trim()) {
      setSaudacao(`${obterSaudacao()}, ${nome}! Bem-vindo(a)!`);
    }
  };

  const limparSaudacao = () => {
    setNome('');
    setSaudacao('');
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Digite seu nome:</Text>
      <TextInput
        style={styles.input}
        placeholder="Seu nome"
        placeholderTextColor="#ccc"
        value={nome}
        onChangeText={setNome}
      />
      <TouchableOpacity style={styles.button} onPress={atualizarSaudacao}>
        <Text style={styles.buttonText}>Confirmar</Text>
      </TouchableOpacity>
      <TouchableOpacity style={[styles.button, styles.buttonDelete]} onPress={limparSaudacao}>
        <Text style={styles.buttonText}>Excluir</Text>
      </TouchableOpacity>
      {saudacao !== '' && <Text style={styles.saudacao}>{saudacao}</Text>}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#2C3E50',
    padding: 20,
  },
  title: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#FFF',
    marginBottom: 10,
  },
  input: {
    width: '80%',
    height: 40,
    borderWidth: 1,
    borderColor: '#FFF',
    borderRadius: 5,
    paddingLeft: 10,
    color: '#FFF',
    backgroundColor: 'rgba(255, 255, 255, 0.2)',
    marginBottom: 15,
  },
  button: {
    backgroundColor: '#27AE60',
    paddingVertical: 10,
    paddingHorizontal: 20,
    borderRadius: 5,
    marginTop: 5,
  },
  buttonDelete: {
    backgroundColor: '#E74C3C',
  },
  buttonText: {
    color: '#FFF',
    fontWeight: 'bold',
  },
  saudacao: {
    fontSize: 22,
    fontWeight: 'bold',
    color: '#FFF',
    textAlign: 'center',
    marginTop: 20,
  },
});

export default App;