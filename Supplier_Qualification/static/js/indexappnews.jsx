const container = document.getElementById("app");



class App extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        data: [],
        loaded: false,
        placeholder: "Loading"
      };
    }
  
    componentDidMount() {
      fetch("/api/news/")
        .then(response => {
          if (response.status > 400) {
            return this.setState(() => {
              return { placeholder: "Something went wrong!" };
            });
          }
          return response.json();
        })
        .then(data => {
          this.setState(() => {
            return {
              data,
              loaded: true
            };
          });
        });
    }
  
    render() {
      return (
        <div>
          {this.state.data.toReversed().map(contact => {
            return (

                    <>
                    
                        <div class="main_window" key={contact.id}>
                                <div class="main_block"></div>

                                <div class="main_window_data_cont">

                                            <div class="main_window_data_cont_title">{contact.dateNews}</div>
                                            <div class="main_window_data_cont_sect">


                                                        <div dangerouslySetInnerHTML={{ __html: contact.dataNews }} />


                                            </div>

                                </div>

                                <div class="main_block"></div>
                        </div>

                        <div class="main_indent"></div></>






            );
          })}
        </div>
      );
    }
  }








ReactDOM.render(
    <App />,
    container
)
