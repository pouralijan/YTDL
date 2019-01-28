import React from 'react';
import axios from 'axios';
import { List, Button, Input } from 'antd';
import 'antd/dist/antd.css';

const Search = Input.Search;

class YTDLLayout extends React.Component{
    layout = ''
    button = (state) => (
        <Button type="primary" loading={state} icon="search" size="large">Search</Button>
    )
    search_button = this.button()
    constructor(props){
        super(props);
        this.state = {
            loading: "",
            videos: []
        }

        
    }

    myFunc(value){
        this.setState({
            loading: "loading"
        })
        this.search_button = this.button(this.state.loading)

        axios.get('http://localhost:8000/api/', {
            params:{
                url: value 
            }
        })
            .then(res => {
                this.setState({
                    videos: res.data,
                    loading: ""
                })
                this.search_button = this.button(this.state.loading)
                console.log(res.data)
            })
    }

    render (){
        return (
            <div>
                <Search
                    placeholder="URL"
                    enterButton={this.search_button}
                    onSearch={value => this.myFunc(value)}
                />
                <List
                    dataSource={this.state.videos}
                    renderItem={
                        item => (
                            <List.Item>
                                {item.type} {item.resolution} {item.abr} {item.codecs} {item.audio_codec}
                                <a href={item.url}>
                                    <Button type="primary" shape="circle" icon="download" size="samall"></Button>
                                </a>
                            </List.Item>
                        )}
                /> 
            </div>
        );
    }
}

export default YTDLLayout;