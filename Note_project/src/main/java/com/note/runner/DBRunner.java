package com.note.runner;

import java.sql.Connection;

import javax.sql.DataSource;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.ApplicationArguments;
import org.springframework.boot.ApplicationRunner;
import org.springframework.stereotype.Component;

@Component
public class DBRunner implements ApplicationRunner{
	@Autowired
	private DataSource dataSource;
	
	//Logger 생성
	private Logger logger = LoggerFactory.getLogger(this.getClass());
	
	@Override
	public void run(ApplicationArguments args) throws Exception {
		logger.debug("데이터 Source 클래스 이름 " + dataSource.getClass().getName());
		Connection connection = dataSource.getConnection();
		logger.debug("DB URL " + connection.getMetaData().getURL());
	}
	
}
