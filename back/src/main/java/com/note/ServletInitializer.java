package com.note;

import org.springframework.boot.builder.SpringApplicationBuilder;
import org.springframework.boot.web.servlet.support.SpringBootServletInitializer;

/**
 *
 * Spring Application 초기화 클래스
 * <p>
 *
 * <pre>
 * 개정이력(Modification Information)·
 * 수정일   수정자    수정내용
 * ------------------------------------
 * 2017. 3. 16.   kt ds     최초작성
 * </pre>
 *
 * @author kt ds A.CoE(yu.chae@kt.com)
 * @since 2017. 3. 16.
 * @version 1.0.0
 * @see
 *
 */
public class ServletInitializer extends SpringBootServletInitializer { 

	protected SpringApplicationBuilder configure(SpringApplicationBuilder application) {
		return application.sources(StarterApplication.class);
	}

}
