# uni_conditional_gradient
conditional gradient method for function minimization



## description
J(u)->inf, u from U

U - выпуклое замкнутое ограниченноре множество из E^n

J(u) from C'(U)

u_0 from U - начальное приближение

Пусть известно k - е прближение u_k from U тогда приращение J(u) в этой точкке можно предстваить в виде:

J(u)-J(u_k) = <J'(u_k), u-u_k> + o(|u - u_k|)

Возьмем линейную часть этого преращение: J_k(u) = <J'(u_k), u - u_k> и определим вспомогательное приближение u1_k from U, inf(U)J_k(u) = J_k(u1_k) = <J'(u_k), u1_k - u_k>

Так как множество U замкнуто и ограничено, а линейная функция J_k(u) непрерывна то точка минимума всегда существцует. Если их больше 1, берем любую.

С поиском u1_k будут проблеммы но мы не лохи. На превью разберемся как-нибудь!!!!!
Будем считать что оно удовлетворяет условиям: u1_k from U, J_k(u1_k)<= min(U)J_k(u) + e_k, e_k>=0, lim(k->inf)e_k->0

Пусть нашли u1_k тогда следующее приближение ищем в виде: u_(k+1) = u_k + a_k * (u1_k - u_k), 0<=a_k<=1

Очевидно в силу выпуклоси U: u_(k+1) from U

Заметим что при u1_k = u_k, u_(k+1) = u_k

Если u1_k взята точное из таблицы, то J_k(u1_k) = J_k(u_k) = 0 = min(U)J_k(u) => <J'(u_k), u-u_k> >= 0 для всех u, что означает что мы достигли минимума

Если значение не точное: -e_k <= min(U)J_k(u)<=J_k(u1_k) = J_k(u_k) = 0 при e_k>0
Тогда проверям условие

a_k возьмем пока 1/(k+1)

# img
![image2](https://github.com/ariolwork/uni_conditional_gradient/blob/master/img/1.png)
![image2](https://github.com/ariolwork/uni_conditional_gradient/blob/master/img/2.png)
![image2](https://github.com/ariolwork/uni_conditional_gradient/blob/master/img/3.png)
