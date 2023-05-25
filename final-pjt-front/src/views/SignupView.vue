<template>
  <div>
    <div class="signupForm">
      <div class="formtitle">
        <p class="title1">회원가입</p>
        <p class="title2">씨네벅스에 오신 것을 환영합니다! 이름과 비밀번호로 간편하게 가입할 수 있어요</p>
      </div>
      <form id="formbody" @submit.prevent="signUp" enctype="multipart/form-data">
        <div class="inputbox">
          <div id="inputusername">
            <label for="username" class="form-label" id="nameform">이름 *</label>
            <input type="text" class="form-control" id="username" v-model="username"
            aria-describedby="inputGroupPrepend2" required placeholder="aiden">
          </div>

          <div class="col-12" id="passwordsection">
            <div class="password1">
              <label for="inputpassword" class="form-label" id="passform">비밀번호 *</label>
              <input
              v-model="password1" @input="lengthCheck" 
              type="password" class="form-control" 
              id="inputpassword" placeholder="비밀번호">
              <p v-if="!long">비밀번호를 4자리 이상 입력해주세요</p>
            </div>

            <div class="password2">
              <label for="password2" class="form-label">비밀번호 확인 *</label>
              <input v-model="password2" type="password" class="form-control" id="password2" placeholder="비밀번호 확인">
              <p>비밀번호를 한 번 더 입력해주세요</p>
            </div>
          </div>

          <button class="upbtn">
            <span>회원가입</span>
          </button>
        </div>
      </form>    
    </div>
  </div>
</template>

<script>
export default {
  name: 'SignupView',
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
      long: '',
    }
  },
  methods: {
    lengthCheck() {
      if (this.password1.length < 5) {
        this.long = false
      } else {
        this.long = true
      }
    },
    fileUpload() {
      this.img = this.$refs.profileimg.files
      console.log(this.img)
    },
    signUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      if (this.password1 != this.password2) {
        alert('비밀번호를 다시 확인해주세요')
      } else {
        const payload = {
          username, password1, password2
        }
        
        this.$store.dispatch('signUp', payload)
      }
    },
  }
}
</script>

<style>
.upbtn {
text-align: center;
margin: auto;
margin-top: 36px;
display: flex;
flex-direction: row;
justify-content: center;
align-items: center;
padding: 12px 18px;
gap: 6px;

width: 92px;
height: 46px;

/* starbucks/sys/light/primary */

background: #006C47;
/* Shadow/XSM */

box-shadow: 0px 1px 2px rgba(16, 24, 40, 0.04);
border-radius: 100px;

/* Inside auto layout */

flex: none;
order: 1;
}

.upbtn span {
  width: 56px;
  height: 22px;

  /* Text Button/Semibold Large */

  font-family: 'Inter';
  font-style: normal;
  font-weight: 600;
  font-size: 15px;
  line-height: 22px;
  /* identical to box height, or 147% */


  /* starbucks/white */

  color: #FFFFFF;


  /* Inside auto layout */

  flex: none;
  order: 0;
  flex-grow: 0;
}
#inputpassword {
  box-sizing: border-box;

  /* Auto layout */

  display: flex;
  flex-direction: row;
  align-items: center;
  padding: 12px 16px;
  gap: 8px;

  width: 268px;
  height: 46px;

  /* starbucks/white */

  background: #FFFFFF;
  /* starbucks/ref/neutral/neutral87 */

  border: 1px solid #DBDAD3;
  /* Shadow/XSM */

  box-shadow: 0px 1px 2px rgba(16, 24, 40, 0.04);
  border-radius: 100px;

  /* Inside auto layout */

  flex: none;
  order: 1;
  align-self: stretch;
  flex-grow: 0;
}

.password1 {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  padding: 0px;
  gap: 8px;

  width: 268px;
  height: 100px;


  /* Inside auto layout */

  flex: none;
  order: 0;
  flex-grow: 1;
}

.password1 p {
width: 268px;
height: 19px;

/* MO/14/Regular */

font-family: 'Spoqa Han Sans Neo';
font-style: normal;
font-weight: 400;
font-size: 14px;
line-height: 19px;
/* identical to box height, or 133% */


/* starbucks/ref/neutral/neutral40 */

color: #5E5F59;


/* Inside auto layout */

flex: none;
order: 2;
align-self: stretch;
flex-grow: 0;
}

.password2 {
display: flex;
flex-direction: column;
align-items: flex-start;
padding: 0px;
gap: 8px;

width: 268px;
height: 100px;


/* Inside auto layout */

flex: none;
order: 1;
flex-grow: 1;
}

.password2 label {
  width: 268px;
  height: 19px;

  /* MO/14/bold */

  font-family: 'Spoqa Han Sans Neo';
  font-style: normal;
  font-weight: 700;
  font-size: 14px;
  line-height: 19px;
  /* identical to box height, or 133% */


  /* Gray/700 */

  color: #272D37;


  /* Inside auto layout */

  flex: none;
  order: 0;
  align-self: stretch;
  flex-grow: 0;
}

.password2 input {
box-sizing: border-box;

/* Auto layout */

display: flex;
flex-direction: row;
align-items: center;
padding: 12px 16px;
gap: 8px;

width: 268px;
height: 46px;

/* starbucks/white */

background: #FFFFFF;
/* starbucks/ref/neutral/neutral87 */

border: 1px solid #DBDAD3;
/* Shadow/XSM */

box-shadow: 0px 1px 2px rgba(16, 24, 40, 0.04);
border-radius: 100px;

/* Inside auto layout */

flex: none;
order: 1;
align-self: stretch;
flex-grow: 0;
}

.password2 p {
  width: 268px;
  height: 19px;

  /* MO/14/Regular */

  font-family: 'Spoqa Han Sans Neo';
  font-style: normal;
  font-weight: 400;
  font-size: 14px;
  line-height: 19px;
  /* identical to box height, or 133% */


  /* starbucks/ref/neutral/neutral40 */

  color: #5E5F59;


  /* Inside auto layout */

  flex: none;
  order: 2;
  align-self: stretch;
  flex-grow: 0;
}

#passwordsection {
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  padding: 0px;
  gap: 16px;

  width: 552px;
  height: 100px;


  /* Inside auto layout */

  flex: none;
  order: 1;
  align-self: stretch;
  flex-grow: 0;
}

.signupForm {
display: flex;
flex-direction: column;
align-items: center;
padding: 0px;
gap: 40px;
margin: auto;

/* position: absolute; */
width: 648px;
height: 538px;
left: calc(50% - 648px/2);
top: calc(50% - 538px/2 + 12px);
}

.formtitle {
  width: 527px;
  height: 87px;


  /* Inside auto layout */

  flex: none;
  order: 0;
  flex-grow: 0;
}

.title1 {
  /* position: absolute; */
  margin: auto;
  margin-bottom: 24px;
  width: 118px;
  height: 39px;
  left: 265px;
  top: 0px;

  /* PC/32 */

  font-family: 'Spoqa Han Sans Neo';
  font-style: normal;
  font-weight: 700;
  font-size: 32px;
  line-height: 39px;
  /* identical to box height, or 122% */


  /* starbucks/ref/neutral/neutral20 */

  color: #30312C;
}

.title2 {
  /* position: absolute; */
  width: 527px;
  height: 24px;
  left: 60.5px;
  top: 63px;

  /* MO/16/Regular */

  font-family: 'Spoqa Han Sans Neo';
  font-style: normal;
  font-weight: 400;
  font-size: 16px;
  line-height: 24px;
  /* identical to box height, or 150% */


  /* starbucks/ref/neutral/neutral50 */

  color: #777771;
}

#formbody {
  box-sizing: border-box;

  /* Auto layout */

  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 56px 0px;
  gap: 56px;

  width: 648px;
  height: 411px;

  /* starbucks/ref/neutral/neutral100 */

  background: #FFFFFF;
  /* starbucks/ref/neutral/neutral94 */

  border: 1px solid #EFEEE6;
  /* Shadow/XSM */

  box-shadow: 0px 1px 2px rgba(16, 24, 40, 0.04);
  border-radius: 24px;

  /* Inside auto layout */

  flex: none;
  order: 1;
  flex-grow: 0;
}

.inputbox {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  padding: 0px 48px;
  gap: 24px;

  width: 648px;
  height: 197px;


  /* Inside auto layout */

  flex: none;
  order: 0;
  align-self: stretch;
  flex-grow: 0;
}

#inputusername {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  padding: 0px;
  gap: 8px;

  width: 552px;
  height: 73px;


  /* Inside auto layout */

  flex: none;
  order: 0;
  align-self: stretch;
  flex-grow: 0;
}

#nameform {
  width: 552px;
  height: 19px;

  /* MO/14/bold */

  font-family: 'Spoqa Han Sans Neo';
  font-style: normal;
  font-weight: 700;
  font-size: 14px;
  line-height: 19px;
  /* identical to box height, or 133% */


  /* Gray/700 */

  color: #272D37;


  /* Inside auto layout */

  flex: none;
  order: 0;
  align-self: stretch;
  flex-grow: 0;
}

#passform {
  width: 268px;
  height: 19px;

  /* MO/14/bold */

  font-family: 'Spoqa Han Sans Neo';
  font-style: normal;
  font-weight: 700;
  font-size: 14px;
  line-height: 19px;
  /* identical to box height, or 133% */


  /* Gray/700 */

  color: #272D37;


  /* Inside auto layout */

  flex: none;
  order: 0;
  align-self: stretch;
  flex-grow: 0;
}

#username {
  box-sizing: border-box;

  /* Auto layout */

  display: flex;
  flex-direction: row;
  align-items: center;
  padding: 12px 16px;
  gap: 8px;

  width: 552px;
  height: 46px;

  /* starbucks/white */

  background: #FFFFFF;
  /* starbucks/ref/neutral/neutral87 */

  border: 1px solid #DBDAD3;
  /* Shadow/XSM */

  box-shadow: 0px 1px 2px rgba(16, 24, 40, 0.04);
  border-radius: 100px;

  /* Inside auto layout */

  flex: none;
  order: 1;
  align-self: stretch;
  flex-grow: 0;
}

#signupform h1 {
  width: 500px;
  text-align: center;
  margin: auto;
  margin-top: 20px;
  margin-bottom: 20px;
}

#sbmbtn {
  margin-bottom: 20px;
}
</style>