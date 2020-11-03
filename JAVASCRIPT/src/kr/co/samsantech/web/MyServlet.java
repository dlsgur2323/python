package kr.co.samsantech.web;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/myservlet")
public class MyServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		String p = request.getParameter("p");
		
		PrintWriter out= response.getWriter();
		out.println("i'm get<br>");
		out.println("p : " + p);
		
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		String p = request.getParameter("p");

		PrintWriter out= response.getWriter();
		out.println("i'm post <br>");
		out.println("p : " + p);
	}

}
