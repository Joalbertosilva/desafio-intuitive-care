<template>
  <div class="container">
    <h1>Operadoras de Planos de Saúde</h1>

    <div class="busca-box">
      <button class="btn" @click="mostrarTodos">Mostrar Todos</button>

      <input
        v-model="busca"
        class="input"
        placeholder="Digite o nome fantasia (ex: UNIMED)"
      />
      <button class="btn" @click="buscarRegistros">Buscar</button>
    </div>

    <table v-if="registros.length" class="table">
      <thead>
        <tr>
          <th v-for="(valor, chave) in registros[0]" :key="chave">{{ chave }}</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(registro, index) in registros" :key="index">
          <td v-for="(valor, chave) in registro" :key="chave">{{ valor }}</td>
        </tr>
      </tbody>
    </table>

    <p v-else class="no-results">Nenhum registro encontrado.</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      registros: [],
      busca: '',
    };
  },
  methods: {
    buscarRegistros() {
     
     const query = `/api/operadoras-saude?nome_fantasia=${encodeURIComponent(this.busca)}`;  
      fetch(query)
        .then(res => res.json())
        .then(data => {
          this.registros = data;
        })
        .catch(err => {
          console.error('Erro ao buscar dados:', err);
        });
    },

    mostrarTodos() {
      this.buscarRegistros();
    }
  },
  mounted() {
    this.buscarRegistros();
  }
};
</script>

<style scoped>
/* Container geral */
.container {
  padding: 2rem;
  font-family: 'Arial', sans-serif;
  background-color: #f9f9f9;
  max-width: 1000px;
  margin: 0 auto;
  border-radius: 8px;
}

/* Títulos */
h1 {
  text-align: center;
  color: #333;
  font-size: 2rem;
  margin-bottom: 1rem;
}

.busca-box {
  display: flex;
  justify-content: center;
  gap: 15px;
  margin-bottom: 1rem;
}

input {
  padding: 0.5rem;
  width: 250px;
  border-radius: 5px;
  border: 1px solid #ccc;
  font-size: 1rem;
}

button {
  padding: 0.5rem 1rem;
  border-radius: 5px;
  border: 1px solid #ccc;
  background-color: #4CAF50;
  color: white;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #45a049;
}

.table {
  margin-top: 20px;
  width: 100%;
  border-collapse: collapse;
}

th, td {
  padding: 12px;
  border: 1px solid #ddd;
  text-align: left;
}

thead {
  background-color: #f2f2f2;
}

tr:nth-child(even) {
  background-color: #f9f9f9;
}

.no-results {
  text-align: center;
  font-size: 1.2rem;
  color: #777;
}
</style>
