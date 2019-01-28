import React from 'react';
import { Layout, Menu } from 'antd';
import 'antd/dist/antd.css';

const { Header } = Layout;

class HeaderLayout extends React.Component{
    render (){
        return (
            <Header>
                <div className="logo"/>
                <Menu
                    theme="dark"
                    mode="horizontal"
                    defaultSelectedKeys={['2']}
                    style={{ lineHeight: '64px' }}
                >
                
                <h1 style={{ color: 'green'}}> YouTube Downloader </h1>
                </Menu>
            </Header>
        );
    }
}

export default HeaderLayout;