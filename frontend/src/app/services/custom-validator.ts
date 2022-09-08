import { AbstractControl, FormControl, ValidationErrors, ValidatorFn, Validators } from '@angular/forms';
export class CustomValidator{


    static ptDate(): ValidatorFn {
        return (control: AbstractControl): Validators | null => {
            let ptDatePattern =  /^(((0[1-9]|[12]\d|3[01])\/(0[13578]|1[02])\/((19|[2-9]\d)\d{2}))|((0[1-9]|[12]\d|30)\/(0[13456789]|1[012])\/((19|[2-9]\d)\d{2}))|((0[1-9]|1\d|2[0-8])\/02\/((19|[2-9]\d)\d{2}))|(29\/02\/((1[6-9]|[2-9]\d)(0[48]|[2468][048]|[13579][26])|((16|[2468][048]|[3579][26])00))))$/g;
 
            if (!control.value.match(ptDatePattern))
                return { "ptDate": true };
     
            return null;
        }
    }

    static isValidCpf(): ValidatorFn {
        return (control: AbstractControl): Validators | null => {
          const cpf = control.value.replace(/[.-]/g,"");
          if (cpf) {
            let numbers, digits, sum, i, result, equalDigits;
            equalDigits = 1;
            if (cpf.length < 11) {
                return { cpfNotValid: true };
            }
   
            for (i = 0; i < cpf.length - 1; i++) {
              if (cpf.charAt(i) !== cpf.charAt(i + 1)) {
                equalDigits = 0;
                break;
              }
            }
   
            if (!equalDigits) {
              numbers = cpf.substring(0, 9);
              digits = cpf.substring(9);
              sum = 0;
              for (i = 10; i > 1; i--) {
                sum += numbers.charAt(10 - i) * i;
              }
   
              result = sum % 11 < 2 ? 0 : 11 - (sum % 11);
   
              if (result !== Number(digits.charAt(0))) {
                return { cpfNotValid: true };
              }
              numbers = cpf.substring(0, 10);
              sum = 0;
   
              for (i = 11; i > 1; i--) {
                sum += numbers.charAt(11 - i) * i;
              }
              result = sum % 11 < 2 ? 0 : 11 - (sum % 11);
   
              if (result !== Number(digits.charAt(1))) {
                return { cpfNotValid: true };
              }
              return null;
            } else {
              return { cpfNotValid: true };
            }
         }
         return null;
     };
   }
}