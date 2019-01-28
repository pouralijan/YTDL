import React from 'react';
import { Layout } from 'antd';
import 'antd/dist/antd.css';


const { Content } = Layout;

class ContentLayout extends React.Component{
    render () {
        return (
            <Content style={{ padding: '0 50px' }}>
                <div style={{ background: '#fff', padding: 24, minHeight: 280 }}>
                    {this.props.children}
                </div>
            </Content>
        );
    }
}

export default ContentLayout;