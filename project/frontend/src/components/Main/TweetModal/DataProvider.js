import React, { Component } from "react";
import PropTypes from "prop-types";
import TweetModal from '../TweetModal/TweetModal';
import Aux from '../../../hoc/Aux/Aux';
import Spinner from '../Spinner/Spinner'
import './TweetModal.css';
class DataProvider extends Component {
  static propTypes = {
    endpoint: PropTypes.string.isRequired,
    render: PropTypes.func.isRequired
  }
  
  state = {
      data: [],
      loaded: false,
      //placeholder: "Loading..."
    };

  componentDidMount() {
    fetch(this.props.endpoint)
      .then(response => {
        if (response.status !== 200) {
          return this.setState({ placeholder: "Something went wrong" });
        }
        return response.json();
      })
      .then(data => this.setState({ data: data, loaded: true }));
  };
  render() {
    const { data, loaded, placeholder } = this.state;
    
    return loaded ? 
    (<Aux>
      <div className="twContainer">
        <TweetModal data={data} />      
      </div>
    </Aux>)
        : (<Spinner />);
  }
}
export default DataProvider;