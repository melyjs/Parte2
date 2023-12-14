export const mainCore = {
    data: function () {
        return {
            form: null,
            form_config_json: "./assets/js/form.pattern.json",
            api_quinceaneras: "https://sheetdb.io/api/v1/dvptdru0jw5rp",
            quinceanera: {
                "name": "",
                "color": "",
                "contacto": "",
                "serie": "",
                "img": "",
                "zodiac-sign": "",
            },

            quinces: null,
            errrLoad: null,
            errorPost: null,
        };
    },
    created: async function () {
        const formData = await fetch(this.form_config_json);
        
        if (!formData.ok) {
            this.errorLoad = 'Error : ${formData.status}';
        }
        this.form = await formData.json();
    },

    methods:{
        getDataHandler: async function (e) {
          e.preventDefault();

          this.quinceanera = {
            id:crypto.randomUUID(),
            ...this.quinceanera,
          };

          const response = await fetch (this.api_quinceaneras,{
            method:"POST",
            body:JSON.stringify(this.quinceanera),
            headers: {
                "Content-Type": "application/json",
            },
          })

          if (!response.ok){
            this.errorPost = 'Falló algo del post. error: ${response.status}';
          }
          else{
            this.errorPost = '${this.quinceanera.contacto} fue cargado en la fecha del ${new Date().toISOString()}';
          }

          this.this.quinceanera={
            "name": "",
            "color": "",
            "contacto": "",
            "serie": "",
            "img": "",
            "zodiac-sign": ""
        }

        },
    },
};