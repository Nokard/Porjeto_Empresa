<template>
  <div id="">

   
    <table class="table">
        <thead>
            
            <th>CNPJ</th>
            <th>MATRIZFILIAL</th>
            <th>RAZAO SOCIAL</th>
            <th>SITUACAO </th>
            
        </thead>
        <tbody>
           <tr v-for="(Empresa,index) in lista" :key="index">            
              
                <td>{{ Empresa.fields.cnpj }}</td>
                <td>{{ Empresa.fields.matrizfilial }}</td>
                <td>{{ Empresa.fields.nm }} </td>
                <td>{{ Empresa.fields.situacao }} </td>                
            </tr>
            {% endfor %}
        </tbody>
    </table>

  </div>
</template>

<script>
export default {

  data() {
    return {
      sortDirection: 'desc',
      lista: []
    }
  },
  mounted() {
    this.$http.get("/home/empresas").then( (req) => this.lista = req.data )
  },
  methods:{
    sort(event, campo){
      event.preventDefault()

      if ( this.sortDirection == "desc" )
      {
          this.sortDirection = "asc"
      }else{
        this.sortDirection = "desc"
      }

      this.lista = _.orderBy(this.lista, campo, this.sortDirection)

    }
  }
}
</script>

<style>

  #exemplo{
      color: red;
  }
</style>

