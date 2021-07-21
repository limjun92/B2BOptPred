## 예외처리 가이드
---
DevPro 에서는 프레임워크 차원에서 예외 처리를 지원하지 않으며, Best Practice 사례를 중심으로 예외 처리에 대한 가이드를 제시하고자 한다.


### 1. 예외는 예외적 상황에만 사용하라

```java
try {
    int i = 0;
    while(true)
        range[i++].climb();
} catch(ArrayIndexOutOfBoundsException e) {
    ....
}
```

- 이 코드에 포함된 무한 루프는 배열 범위 밖에 있는 첫 번째 요소를 참조하는 순간에 발생하는 ArrayIndexOutOfBoundsException예뢰를 감지하고 무시하는 과정을 통해 종료된다.
- **예외는 예외적인 상황에만 사용해야지, 평상시 제어 흐름에 이용해서는 안된다.**
- 잘 설계된 API는 클라이언트에게 평상시 제어 흐름의 일부로 예외를 사용하도록 강요해서는 안 된다.
- 특정한 예측 불가능 조건이 만족될 때만 호출할 수 있는 “상태 종속적” 메서드를 가진 클래스에는 보통 해당 메서드를 호출해도 되는지를 알기 위한 “상태 검사” 메서드가 별도로 갖춰져 있다.
예를 들어 Iterator 인터페이스에는 상태 종속적 메서드 next가 있고, 상태 검사 메서드 hasNext가 있다. Iterator에 hasNext 메서드가 없었다면 클라이언트는 어쩔 수 없이 아래와 같은 코드를 만들어야 했을 것이다.

```java
// 아래와 같이 하지 말것
try {
    Iterator<Foo> i = collection.iterator();
    while(true) {
        Foo foo = i.next();
    }
}catch (NoSuchElementException e) { }
```
- 상태 검사 메서드를 제공하기 싫다면, 부적절한 상태의 객체에 상태 종속적 메서드를 호출하면 null 같은 특이값이 반환되도록 구현하는 방법도 있다. 
- 그러나 이 기법은 Iterator에는 사용할 수 없는데, null은 next 메서드의 정상적 반환값 가운데 하나이기 때문이다. 
- **외부적인 동기화 메커니즘 없이 병렬적으로 사용될 수 있는 객체거나, 외부적인 요인으로 상태 변화가 일어날 수 있는 객체라면 반드시 특이값 방식으로 구현해야 한다.** 
- 상태 검사 메서드를 호출한 다음 상태 종속적 메서드를 호출하기까지의 시간 동안 객체 상태가 변할 수 있기 때문이다.


### 2. 복구 가능 상태에는 점검지정 예외(Checked Exception)를 사용하고, 프로그래밍 오류에는 실행시점 예외(RuntimeException)를 이용하라

자바는 세 가지 종류의 ‘throwable’을 제공한다. 
- 점검지정 에외(checked exception), 실행시점 예외(runtime exception), 그리고 오류(error)다. 

점검지정 예외를 사용할 것인지 아니면 무점검 예외를 사용할 것인지에 대한 가장 기본적인 규칙은, **호출자(caller) 측에서 복구할 것으로 여겨지는 상황에 대해서는 점검지정 예외를 이용해야 한다는 것이다.** 
점검지정 예외를 던지는 메서드를 호출한 클라이언트는 해당 예외를 catch 절 안에서 처리하든지, 아니면 계속 밖으로 던져지도록 놔두든지 해야 한다. 
따라서 메서드에 선언된 점검지정 예외는 메서드를 호출하면 해당 예외와 관계된 상황이 발생할 수 있음을 API 사용자에게 알리는 구실을 한다.

무점검(unchecked) ‘throwable’에는 실행시점 에외와 오류 두 가지가 있으며, 동작 방식은 같다. 프로그램이 무점검 예외나 오류를 던진다는 것은 복구가 불가능한 상황에 직면했다는 뜻으로, 더 진행해 봐야 득보다 실이 더 크다는 뜻이다.

**프로그래밍 오류를 표현할 때는 실행시점 예외를 사용하라.**

대부분의 실행시점 예외는 선행조건 위반을 나타낸다. 즉, 클라이언트가 API 명세에 기술된 규약을 지키지 않았다는 뜻이다. 요약하자면 복구 가능한 상태에는 점검지정 예외를 사용하고, 프로그래밍 오류를 나타내고 싶을 때는 실행시점 예외를 사용하라.


### 3. 불필요한 점검지정 예외(CheckedException) 사용은 피하라

점검지정 예외는 프로그래머로 하여금 예외적인 상황을 처리하도록 강제함으로써 안정성을 높인다. 하지만 너무 남발하면 사용하기 불편한 API가 될 수 있다는 뜻이기도 하다.

API를 제대로 이용해도 예외 상황이 벌어지는 것을 막을 수 없을 때, 그리고 API 사용자가 예외 상황에 대한 조치를 취할 수 있을 때는, 그 정도의 부담은 참을 수 있을 것이다. 하지만 이 조건 가운데 어디에도 해당되지 않을 때는 무점검 예외를 이용하는 것이 좋다.

```java
} catch (TheCheckedException e) {
    throw new AssertionError(); // Cant't happen ! 
}

아래 코드는 어떤가? 

} catch (TheCheckedException e) {
    e.printStrackTrace(); // Oh well. we lose. 
    System.exit(1);
}
```
API 사용자가 이보다 좋은 코드를 만들 수 없다면, 무점검 예외가 적당하다. 이 테스트를 통과하지 못하는 예외의 사례로는 CloneNotSupportedException이 있다. 이 예외는 Cloneable 인터페이스를 구현하지 않은 객체에 Object.clone 메서드를 호출하면 발생하는 예외다. 실제로는, 이 예외를 처리하는 catch 블록이 실행되었다는 것은, 확증이 실패했다는 것이나 마찬가지다. 그런 특성에 어울리지 않게 점검지정 예외로 선언되어 있다는 것이 문제인데, 프로그래머 입장에서는 반갑지 않은 일이다. 프로그램만 복잡해지기 때문이다.

메서드가 던지는 점검지정 예외가 하나뿐일 때 프로그래머가 느끼게 되는 부담은 큰 편이다. 그 하나의 catch 블록 때문에 try 블록 안에서 메서드를 호출해야 하는 것이다. 이런 상황에 처하면, 점검지정 예외를 없앨 방법이 없을지 고민해보는 것이 좋다. **점검지정 예외를 무점검 예외로 바꾸는 한 가지 방법은, 예외를 던지는 메서드를 둘로 나눠서 첫 번째 메서드가 boolean 값을 반환하도록 만드는 것이다.**

```java
// 예외를 점검하도록 지정된 메서드 호출 
try {
    obj.action(args);
} catch(TheCheckedException e){
    // 예외적 상황 처리
    …
}
```

앞서 설명한 대로 메서드를 리팩토링하면 이 코드는 아래와 같이 바뀐다.

```java
// 상태 검사 메서드를 거쳐서 무점검 예외 메서드 호출
if (obj.actionPermitted(args)) {
    obj.action(args);
} else {
    // 예외적 상황 처리
    …
}
```

메서드 호출 순서가 이전 방식에 비해 더 깔끔하다고 말하기는 어려우나, 더 유연한 API가 되었음은 사실이다. action 호출이 항상 성공하리라고 확신하거나, 설사 실패해서 스레드가 죽어도 상관없다면 위의 코드는 obj.action(args) 한 줄로 줄일 수 있다. 하지만 그 결과로 만들어지는 예외처리 1번룰(예외는 예외적 상황에만 적용하라)에서 설명한 상태 검사 메서드와 본질적으로 같기 때문에 동일한 문제를 갖는다. 외부적인 동기화 수단 없이 병렬적으로 이용될 가능성이 있는 객체거나, 외부에서 그 상태를 바꿀 가능성이 있는 객체라면 방금 설명한 리팩토링 기법은 적용할 수 없다. actionPermitted를 호출하고 action을 미처 호출하기 전에 객체의 상태가 바뀔 수도 있기 때문이다.


### 4. 표준 예외를 사용하라

**가장 널리 재사용 되는 예외는 IllegalArgumentException이다.** 잘못된 값을 인자로 전달했을 때 일반적으로 발생하는 예외다. 널리 쓰이는 또 다른 예외로는 IllegalStateException이 있다. 현재 객체 상태로는 호출 할 수 없는 메서드를 호출했을 때 일반적으로 발생하는 예외다. 예를 들어 아직 적절히 초기화되지 않은 객체를 사용하려고 시도하면 이 예외가 발생해야 할 것이다.

모든 잘못된 메서드 호출은 결국 잘못된 인자나 잘못된 상태에 관계된 것이라 이해할 수 있다. 하지만 특정 부류의 잘못된 인자나 상태에 표준적으로 이용되는 예외들도 있다. null 인자를 받으면 안되는 메서드에 null을 전달한 경우, 관습적으로는 IllegalArgumentException 대신 **NullPointerException** 이 발생해야 한다. 이와 비슷하게, 어떤 sequence의 첨자를 나타내는 인자에 참조 가능 범위를 벗어난 값이 전달되었을 때는 **IndexOutOfBoundsException** 이 발생해야 한다

일반적 용도의 예외 가운데 알아둘 만한 것으로는 **ConcurrentModificationException** 도 있다. 하나의 스레드만 사용하도록 설계된 객체나, 외부적인 동기화 수단과 함께 이용되어야 하는 객체를 여러 스레드가 동시에 변경하려 하는 경우에 발생해야 하는 예외다. 또 **UnsupportedOperationException** 도 알아두면 좋다. 어떤 객체가 호출된 메서드를 지원하지 않을 때 발생하는 예외다. 다른 예외들에 비해 사용 빈도가 아주 낮은데, 대부분의 객체는 자기가 구현하는 메서드를 지원하는 것이 보통이기 때문이다. 이 예외는 인터페이스에 정의된 선택적 메서드 가운데 하나 이상을 구현하지 않을 경우에 사용한다.

재사용 할 수 있는 예외라 생각된다면, 사용하도록 하라. 하지만 예외를 발생시키는 조건이 해당 예외의 문서에 기술된 것과 일치해야 한다. 마지막으로 어떤 예외를 재사용하면 좋을 지 결정하는 것은 엄밀한 과학적 절차를 따르지 않는다. 위의 표에 나열한 용례조차도 상호 배제적이지 않다.

#### 장점
- 배우기 쉽고 사용하기 편리
- 가독성 우수
- 예외 클래스 수를 줄이면서 프로그램 메모리와 클래스 로딩 시간 단축

#### 가장 널리 사용되는 예외

| 예외객체 | 설명 |
| ------ | ------ |
| IlleagalArgumentException | 인자의 값이 잘못 된 경우 |
| IlleagalStateException | 객체 상태가 메소드 호출을 처리하기 적절치 않을 경우 |
| NullPointerException | 널값을 받으면 안되는 인자에 널값이 전달될 경우 |
| IndexOutOfBoundsException | 인자로 주어진 첨자가 허용 범위를 벗어난 경우 |
| ConcurrentModificationException | 병렬적 사용이 금지된 객체에 대한 병렬 접근이 탐지되었을 경우 |
| UnsupportedOperationException | 객체가 해당 메소드를 지원하지 않을 경우 |



### 5. 추상화 수준에 맞는 예외를 던져라

상위 계층에서는 하위 계층에서 발생하는 예외를 반드시 받아서 상위 계층 추상화 수준에 맞는 예외로 바꿔서 던져야 한다. 이 숙어를 ‘예외 변환’이라 부른다.

```java
// 예외 변환
try {
    // 낮은 수준의 추상화 계층 이용
    ...
} catch (LowerLevelException e) {
    throw new HigherLevelException(…);
}
```

exception translation 예제

```java
public void add() throws DuplicateUserIdException {
    try {
        // JDBC를 이용해 user 정보를 DB에 추가하는 코드 또는
        // 그런 기능이 있는 다른 SQLException을 던지는 메서르르 호출하는 코드 
    }catch (SQLException e){
        if(e.getErrorCode() == MysqlErrorNumbers.ER_DUP_ENTRY)
            throw new DuplicateUserIdException(e); 
    }
}
```
위의 코드를 보면 예외 연결(exception chaining)도 포함되어 있다. 하위 계층에서 발생한 예제 정보가 상위 계층 예외를 발생시킨 문제를 디버깅하는 데 유용할 때 사용한다.

```java
// 예외 연결 
try {
    // 낮은 수준의 추상화 계층 이용
    ...
} catch (LowerLevelException cause) {
    throw new HigherLevelException(cause);
}
```

상위 계층 예외 HigherLevelException의 생성자는 문제의 ‘원인’을 예외 연결을 지원하는 상위 클래스 생성자에 넘긴다. 해당 인자는 결국 Throwable의 예외 연결 지원 생성자에 전달된다.

```java
// 예외 연결 지원 생성자를 갖춘 예외
class HigherLevelException extends Exception {
    HigherLevelException (Throwable cause){
        super(cause);
    }
}
```

부분의 표준 예외들은 예외 연결 지원 생성자를 구비하고 있다.
예외 처리의 제일 좋은 방법은 하위 계층에서 예외가 생기지 않도록 하는 것이다. 하위 계층 메서드에서 예외가 발생하는 것을 막을 수 없다면 그 다음으로 좋은 방법은 하위 계층에서 생기는 문제를 상위 계층 메서드 호출자로부터 격리시키는 것이다. 하위 계층에서 발생하는 예외를 어떤 식으로든 처리해 버리는 것이다. 그래야 하는 상황이라면 java.util.logging 같은 기능을 활용해서 로그를 남기면 좋을 것이다. 클라이언트나 최종 사용자에게는 문제를 감추지만, 관리자는 나중에 분석할 수 있도록 하는 것이다.


### 6. 메서드에서 던져지는 모든 예외에 대해 문서를 남겨라

점검지정 예외는 독립적으로 선언하고, 해당 예외가 발생하는 상황은 Javadoc @throws 태그를 사용해서 정확하게 밝혀라. 메서드가 던질 가능성이 있는 모든 예외를 문서로 남겨라. 점검지정 예외뿐만 아니라, 무점검 예외에도 문서를 만들라(무점검 예외는 보통 프로그래밍 오류를 나타낸다). 점검지정 예외는 메서드의 throws 절에 나열하고, 무점검 예외는 throws 절에는 적지마라.


### 7. 어떤 오류인지를 드러내는 정보를 상세한 메세지에 담으라

쉽게 재현할 수 없는 오류라면, stack trace 이상의 정보를 얻기 어렵거나 불가능하다. 그래서 예외의 상세 메세지에는 원인 분석에 이용될 오류 정보가 포착되어 있어야 한다. **오류 정보를 포착해 내기 위해서는, 오류의 상세 메세지에 “예외에 관계된” 모든 인자와 필드의 값을 포함시켜야 한다.**

오류를 적절히 포착하는 정보를 상세 메세지에 담는 한 가지 방법은, 상세한 정보를 요구하는 생성자를 만드는 것이다.
```java
/**
* Construct an IndexOutOfBoundsException.
*
* @param lowerBound the lowest legal index value.
* @param upperBound the highest legal index value plus one.
* @param index the actual index value.
*/
public IndexOutOfBoundsException(int lowerBound, int upperBound, int index) {
    // Generate a detail message that captures the failure
    super("Lower bound: " + lowerBound +
            ", Upper bound: " + upperBound +
            ", Index: " + index);
    // Save failure information for programmatic access
    this.lowerBound = lowerBound;
    this.upperBound = upperBound;
    this.index = index;
}
```

### 8. 실패 원자성 달성을 위해 노력하라

일반적으로 이야기해서 호출이 정상적으로 처리되지 못한 객체의 상태는, 메서드 호출 전 상태와 동일해야 한다. 이 속성을 만족하는 메서드는 **실패 원자성을 갖추었다고 한다.**

실패 원자성을 달성하는 방법은 여러 가지다. 가장 간단한 방법은 **변경 불가능 객체로 설계**하는 것이다. 변경 불가능한 객체의 경우, 실패 원자성은 덤이다. 변경 가능한 객체의 경우에는 실제 연산을 수행하기 전에 **인자 유효성(validity)을 검사**하는 것이 가장 보편적인 방법이다. 객체를 변경하는 도중에 예외가 발생하는 것을 막아준다.

```java
public Object pop() {
    if(size == 0)
        throw new EmptyStackException();
    Object result = elements[--size];
    elements[size] = null;
    return result;
}
```

위 코드를 보면, 빈 스택에서 뭔가를 뽑아내려 하면, 굳이 첫 두줄이 없어도 예외가 나긴 한다. 하지만 첫 두 줄이 없으면 size 필드의 일관성이 깨져서 음수로 바뀌게 된다. 그러니 이 메서드를 다시 호출하면 계속 문제가 생길 것이다. 게다가, 첫 두 줄이 없을 때 발생하는 예외는 해당 클래스에는 어울리지 않는다.

이와 밀접한 관련이 있는 또 다른 접근법 하나는, **실패할 가능성이 있는 코드를 전부 객체 상태를 바꾸는 코드 앞에 배치하는 것**이다. 예를 들어 TreeMap에 추가할 원소는 해당 TreeMap의 순서대로 비교가 가능한 자료형이어야 한다. 엉뚱한 자료형의 원소를 넣으려고 하면, 트리를 실제로 변경하기 전에 트리 안에서 해당 원소를 찾다가 ClassCastException이 발생할 것이다.

사용 빈도가 훨씬 낮은 세 번째 접근법은 연산 수행 도중에 발생하는 오류를 가로채는 복구 코드를 작성하는 것이다. 이 복구 코드는 연산이 시작되기 이전 상태로 객체를 되돌린다(roll back)

마지막 접근법은, 객체의 임시 복사본상에서 필요한 연산을 수행하고, 연산이 끝난 다음에 임시 복사본의 내용으로 객체 상태를 바꾸는 것이다. 예를 들어 Collections.sort는 원소들을 참조하는 비용을 줄이기 위해, 인자로 주어진 리스트를 정렬하기 전에 배열에 복사한다. 성능 문제 때문에 내린 조치인데, 그 덕에 정렬이 실패해도 원래 리스트에는 아무런 손상이 가지 않는다.

실패 원자성은 일반적으로 권장되는 덕목이지만 언제나 달성할 수 있는 것은 아니다. 명심할 것은, 예외와는 달리 오류(error)는 복구가 불가능하며, 오류를 던지는 경우에는 실패 원자성을 보존하려 애쓸 필요가 없다는 점이다.


### 9. 예외를 무시하지 마라

```java
// catch 블록을 비워 놓으면 예외는 무시된다
try {
    ...
}catch(SomeException e){

}
```

**빈 catch 블록은 예외를 선언한 목적, 그러니까 예외적 상황을 반드시 처리하도록 강제한다는 목적에 배치된다.**

예외를 무시해도 괜찮은 경우를 하나 예로 들자면, FileInputStream을 닫는 경우일 것이다. 파일 상태를 바꾸지 않았고 그래서 복구 작업을 할 필요도 없으며, 필요한 정보는 파일에서 모두 읽었으니 진행 중인 연산을 중단할 이유도 없다. 하지만 그렇더라도 로그는 남겨두는 것이 좋다. 그래야 예외가 자주 발생하는 것을 알았을 때 그 원인을 분석해 볼 수 있기 때문이다.


### 10. 있으나마나한 catch 절 쓰지 않기

아래와 같이 catch절에서 아무 작업도 없이 바로 throw 를 하는 코드는 있나마나한 코드입니다.
```java
try {
    process();
} catch (IOException e) {
    throw e
}
```

아래 코드와 그냥 똑같습니다.
```java
process();
```

Exception을 무시하는것보다는 위험은 적지만, 그래도 굳이 불필요한 코드만 추가한 것입니다. catch절에는 예외 흐름에 적합한 구현코드가 있어야 합니다. 로깅이나 Layer에 적합한 Exception 변환 등도 그 예입니다.


### 11. e.printStackTrace() 보다는 로거 사용

Exception을 기록으로 남기고 끝낼 경우에라도 로깅 프레임워크를 사용하는 편이 좋습니다.

```java
// 비추천
try {
    process();
} catch (IOException e) {
    e.printStackTrace()
}
```

-->
```java
// 추천
try {
    process();
} catch (IOException e) {
    log.error("fail to process file", e);
}
```

Tomcat에서 e.printStackTrace()로 콘솔에 찍힌 값은 {TOMCAT_HOME}/logs/catalina.out 에만 남습니다. 로깅 프레임워크를 이용하면 파일을 쪼개는 정책을 설정할 수 있고, 여러 서버의 로그를 한곳에서 모아서 보는 시스템을 활요할 수도 있습니다.

log.error()메서드에 Exception객체를 직접 넘기는 e.printStackTrace()처럼 Exception의 스택도 모두 남겨줍니다. 에러의 추적성을 높이기 위해서는 e.toString()이나 e.getMessage()로 마지막 메시지만 남기기보다는 전체 에러 스택을 다 넘기는 편이 좋습니다.


### 12. 여러가지 상황에서의 예외처리 

- alternative return value가 있는 경우에는 Checked exception
- data connection 생성 실패와 같이 뭔가 크게 잘못 되고 있어서 호출한 쪽에서 아무도 이를 처리할 수 없을 때는 Runtime exception
- 소수의 호출자만이 Exception을 받아서 처리해야 할 때도 Runtime exception
- 불명확하면 Runtime exception
- Be specific, Throw Early, Catch Late의 3가지 원칙을 지킬것
- Checked Exception을 RuntimeException으로 감싸기, throws 절에 RuntimeException이라도 선언해주기 등의 기법을 추천
- Client code가 할 일이 있을 때는 checked, 없을 때는 unchecked. progamming error에는 unchecked exception
- 적절한 캡슐화. 비지니스 layer에서 SqlException을 던지지 말것
- 에러메시지에 도움이 되는 정보를 더할 수 없다면, Exception을 잡지마라. Exception을 잡았으면 기록하라
- public 메소드에서 던지는 Exception은 해당 패키지에 소속된 클래스일것, 다른 패키지에서는 이를 부를 때를 Exception을 전파시키지 말고 그 패키지의 Exception으로 감쌀 것을 추천
