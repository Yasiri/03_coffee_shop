import { Component, OnInit } from '@angular/core';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-user-page',
  templateUrl: './user-page.page.html',
  styleUrls: ['./user-page.page.scss'],
})
export class UserPagePage implements OnInit {
  loginURL: string;
  logoutURL: any;

  constructor(public auth: AuthService) {
    // this.loginURL = auth.build_login_link('/tabs/user-page');
    if (this.checkLogout() === true) {
      this.loginURL = auth.build_login_link('/tabs/user-page');
    } else {
      this.logoutURL = auth.build_logout_link();
    }
  }

  ngOnInit() {
  }

  checkLogout() {
    const logOutToken = localStorage.getItem('JWTS_LOCAL_KEY');
    if (logOutToken) {
      return false;
    } else {
      return true;
    }
  }

}
