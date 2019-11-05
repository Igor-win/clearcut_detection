import React, { Component } from 'react';

import { ReactComponent as Logo } from '../../assets/images/logo.svg';

import Switch from '../Switch';

import './style.css';

class Sidebar extends Component {
  state = {
    isOpened: true
  };

  handleClick = () => this.setState({ isOpened: !this.state.isOpened });

  render() {
    const { isOpened } = this.state;
    const { children } = this.props;

    return (
      <aside className="sidebar">
        <header className="sidebar-header">
          <div className="logo">
            <Logo />
          </div>
          <Switch state={isOpened} handleClick={this.handleClick} />
        </header>
        {isOpened && <div className="sidebar-body">{children}</div>}
      </aside>
    );
  }
}

export default Sidebar;
