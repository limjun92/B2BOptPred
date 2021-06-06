package com.note.testpy;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import org.apache.commons.exec.CommandLine;
import org.apache.commons.exec.DefaultExecutor;
import org.apache.commons.exec.PumpStreamHandler;

import java.io.ByteArrayOutputStream;
import java.io.IOException;

@RestController
@RequestMapping("/testpy")
public class PythonController {
	
	@GetMapping("/print")
	public ResponseEntity<?> getUser() {
		String re = "";
		System.out.println("=============================");
		System.out.println("Python Call");
        String[] command = new String[4];
        command[0] = "python";
        //command[1] = "/Users/limju/OneDrive/바탕 화면/신입사원역량강화프로젝트/test.py";
        command[1] = "/Users/limju/OneDrive/바탕 화면/신입사원역량강화프로젝트/test-DESKTOP-9Q38GK1.py";
        command[2] = "10";
        command[3] = "20";
        try {
        	re = execPython(command);
        } catch (Exception e) {
            e.printStackTrace();
        }
        return ResponseEntity.status(HttpStatus.OK).body(re);
	}
	
	public static String execPython(String[] command) throws IOException, InterruptedException {
		System.out.println("??");
		CommandLine commandLine = CommandLine.parse(command[0]);
	    System.out.println("=============");
	    for (int i = 1, n = command.length; i < n; i++) {
	        commandLine.addArgument(command[i]);
	    }

	    ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
	    PumpStreamHandler pumpStreamHandler = new PumpStreamHandler(outputStream);
	    DefaultExecutor executor = new DefaultExecutor();
	    executor.setStreamHandler(pumpStreamHandler);
	    int result = executor.execute(commandLine);
	    System.out.println("result: " + result);
	    System.out.println("output: " + outputStream.toString());
	    return outputStream.toString();

	}    
}


