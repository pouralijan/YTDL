import React from 'react';
import 'antd/dist/antd.css';
import { Layout } from 'antd';
const { Footer } = Layout;

class FooterLayout extends React.Component{
    render (){
        return (
            <Footer style={{ textAlign: 'center' }}>
                ©2018 Created by Hassan Pouralijan
            </Footer>
        );
    }
}

export default FooterLayout;