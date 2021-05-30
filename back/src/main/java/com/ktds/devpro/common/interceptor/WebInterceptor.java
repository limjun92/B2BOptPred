package com.ktds.devpro.common.interceptor;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.ModelAndView;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * 
 * Web 경로 접근 인터셉터
 * <p>
 * <pre>
 * 개정이력(Modification Information)·
 * 수정일   수정자    수정내용
 * ------------------------------------
 * 2017. 3. 17.    kt ds     최초작성
 * </pre>
 *  
 * @author kt ds A.CoE(yu.chae@kt.com)
 * @since 2017. 3. 17.
 * @version 1.0.0
 * @see 
 *
 */
public class WebInterceptor implements HandlerInterceptor {

	Logger logger = LoggerFactory.getLogger(this.getClass());

	@Override
	public void afterCompletion(HttpServletRequest request, HttpServletResponse response, Object object,
			Exception exception) throws Exception {
		logger.debug("WebInterceptor.afterCompletion()");
		
	}

	@Override
	public void postHandle(HttpServletRequest request, HttpServletResponse response, Object object,
			ModelAndView exception) throws Exception {
		logger.debug("WebInterceptor.postHandle()");

	}

	@Override
	public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object exception)
			throws Exception {

		// Context Path
		String contextPath = request.getContextPath();

		// Context Path를 제외한 URI
		String uri = request.getRequestURI().replaceAll(contextPath, "");

		// QueryString
		String queryString = request.getQueryString();

		logger.debug("WebInterceptor.preHandle() contextPath = {} " , contextPath);
		logger.debug("WebInterceptor.preHandle() uri = {} " , uri);
		logger.debug("WebInterceptor.preHandle() queryString = {} " , queryString);

		return true;
	}

}
